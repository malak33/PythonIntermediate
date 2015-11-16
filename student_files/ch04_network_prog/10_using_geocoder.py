from pygeocoder import Geocoder

def get_results(address):
    results = Geocoder.geocode(address)
    return results.raw

def get_coordinates(address):
    results = Geocoder.geocode(address)
    return results[0].coordinates

def get_zip_code(address):
    results = Geocoder.geocode(address)
    return results[0].postal_code

address = 'Walt Disney World, Lake Buena Vista, FL'

coordinates = get_coordinates(address)
print('Coordinates: {0}'.format(coordinates))
zip_code = get_zip_code(address)
print('Zip Code: {0}'.format(zip_code))
raw = get_results(address)
print('Raw data: {0}'.format(raw))