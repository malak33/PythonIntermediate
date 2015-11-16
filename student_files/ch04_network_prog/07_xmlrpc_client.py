import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:8052/')

search_abbr = input('Enter airport abbreviation (enter when done): ')

while search_abbr:
    print('Airport name: {0}'.format(proxy.search_airport(search_abbr)))
    search_abbr = input('Enter airport abbreviation (enter when done): ')
