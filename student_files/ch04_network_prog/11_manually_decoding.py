import http.client
import json
from urllib.parse import quote_plus

url = '/maps/api/geocode/json?address={0}&sensor=false'
address = 'Walt Disney World, Lake Buena Vista, FL'

path = url.format(quote_plus(address))
connection = http.client.HTTPConnection('maps.google.com')
connection.request('GET', path)

raw_json_response = connection.getresponse().read()
json_response = raw_json_response.decode()

print(json_response)

geo_object = json.loads(json_response)
print(geo_object['results'][0]['address_components'][0]['long_name'])



