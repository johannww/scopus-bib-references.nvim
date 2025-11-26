#!/usr/bin/env python3
import sys
import re
import ieee_doi_extract
import springer_doi_extract
import mdpi_doi_extract
import pybliometrics
pybliometrics.scopus.init()
from pybliometrics.scopus import AbstractRetrieval

def get_bibtex_conference(ab: AbstractRetrieval):
    """Bibliographic entry in BibTeX format.

    Raises
    ------
    ValueError
        If the item's aggregationType is not Conference.
    """
    if ab.aggregationType != 'Conference Proceeding':
        raise ValueError('Only Conference Proceeding articles supported.')
    # Item key
    year = ab.coverDate[0:4]
    first = ab.title.split()[0].title()
    last = ab.title.split()[-1].title()
    key = ''.join([ab.authors[0].surname, year, first, last])
    # Authors
    authors = ' and '.join([f"{a.given_name} {a.surname}"
                            for a in ab.authors])
    # Pages
    if ab.pageRange:
        pages = ab.pageRange
    elif ab.startingPage:
        pages = f'{ab.startingPage}-{ab.endingPage}'
    else:
        pages = '-'
    # All information
    bib = f"@article{{{key},\n  author = {{{authors}}},\n  title = "\
          f"{{{{{ab.title}}}}},\n  journal = {{{ab.publicationName}}},"\
          f"\n  year = {{{year}}},\n  volume = {{}},\n  "\
          f"number = {{}},\n  pages = {{{pages}}}"
    # DOI
    if ab.doi:
        bib += f",\n  doi = {{{ab.doi}}}"
    bib += "}"
    return bib


# Document-specific information
article_url = sys.argv[1]
is_sciencedirect = article_url.find("sciencedirect.com") != -1
is_scopus = article_url.find("scopus.com") != -1
is_ieee = article_url.find("ieeexplore.ieee.org") != -1
is_springer = article_url.find("link.springer.com") != -1
is_mdpi = article_url.find("mdpi.com") != -1
is_acm = article_url.find("acm.org") != -1
is_doi = article_url.find("doi.org") != -1
if is_sciencedirect:
    article_url = article_url.split("?")[0]
    article_id = article_url.split("pii/")[1]
    id_type = "pii"
elif is_scopus:
    # matches = re.match(r"https://www.scopus.com/record/.*eid=(.*?)&", article_url)
    # id_type = "eid"
    matches = re.match(r"https://www.scopus.com/pages/publications/(.*?)$", article_url)
    article_id = matches.group(1)
    id_type = "scopus_id"
elif is_ieee:
    article_id = ieee_doi_extract.extract_doi(article_url)
    id_type = "doi"
elif is_springer:
    article_id = springer_doi_extract.extract_doi(article_url)
    id_type = "doi"
elif is_mdpi:
    print("ismdpi")
    article_id = mdpi_doi_extract.extract_doi(article_url)
    print("article id", article_id)
    id_type = "doi"
elif is_acm:
    matches = re.match(r"https://dl.acm.org/doi.*?/(\d.*$)", article_url)
    article_id = matches.group(1)
    id_type = "doi"
elif is_doi:
    article_id = article_url.split("doi.org/")[1]
    id_type = "doi"
else:
    print("URL not recognized")
    exit(1)

ab = AbstractRetrieval(article_id, view = "FULL", id_type = id_type)
if ab.aggregationType == 'Journal':
    bibtex = ab.get_bibtex()
elif ab.aggregationType == 'Conference Proceeding':
    bibtex = get_bibtex_conference(ab)
else:
    print("Only Journal articles and Conference proceedings supported.")
    exit(1)

if ab.authkeywords:
    brackets_at_end = bibtex.rfind("}")
    bibtex = bibtex[:brackets_at_end] + ",\n  keywords = {" + ", ".join(ab.authkeywords) + "}}"

if ab.scopus_link:
    brackets_at_end = bibtex.rfind("}")
    if is_sciencedirect or is_ieee or is_springer or is_mdpi or is_doi:
        bibtex = bibtex[:brackets_at_end] + ",\n  url = {" + article_url + "}}"
    else:
        bibtex = bibtex[:brackets_at_end] + ",\n  url = {" + ab.scopus_link + "}}"

print(bibtex)
