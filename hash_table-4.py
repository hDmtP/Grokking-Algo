cached = {}

def get_data_from_server(url):
    return True

def get_page(url):
    if cached.get(url):
        return cached[url]
    else:
        data = get_data_from_server(url)
        cached[url] = data
        return cached[url]

