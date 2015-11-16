from urllib.request import urlopen

def retrieve(url):
    return urlopen(url).read()

results = retrieve('http://www.google.com')
print(results.decode())

