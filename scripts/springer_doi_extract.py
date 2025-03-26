def extract_doi(url):
    split_url = url.split('/')
    if len(split_url) < 2:
        print("springer URL is invalid.")
        exit(1)
    last_slash = split_url[-1]
    before_last_slash = split_url[-2]

    return before_last_slash + '/' + last_slash
