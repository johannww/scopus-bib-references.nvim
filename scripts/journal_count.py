import sys
import bibtexparser

journals = {}

def print_descending_journal_count(bibtex_file):
    with open(bibtex_file) as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    entries = bib_database.entries

    for entry in entries:
        if 'journal' not in entry:
            continue
        journalname = entry['journal']
        if journalname in journals:
            journals[journalname] += 1
        else:
            journals[journalname] = 1

    sorted_journals = sorted(journals.items(), key=lambda x: x[1], reverse=True)
    for journal, count in sorted_journals:
        print(f'{journal}: {count}')

# Usage example
bibtex_file = sys.argv[1]
print_descending_journal_count(bibtex_file)

