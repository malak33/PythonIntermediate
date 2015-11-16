from urllib.request import urlopen

def page(url):
    def get():
        return urlopen(url).read()
    return get

get_google = page('http://www.google.com')
page_data = get_google()
print(page_data)