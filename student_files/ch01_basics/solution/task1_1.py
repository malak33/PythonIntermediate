"""

      task1_1.py   -   Python Basics Overview

      Reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

"""
import locale
import os


working_dir = '../../resources'
city_data = 'cities15000.txt'
cities = {}
locale.setlocale(locale.LC_ALL, '')

sort_by_population = lambda k: cities[k][0]
sort_by_elevation = lambda k: cities[k][1]


def format_groupings(value):
    return locale.format('%d', value, grouping=True)

try:
    with open(os.path.join(working_dir, city_data), encoding='utf8') as cities_file:
        for line in cities_file:
            city_record = line.strip().split('\t')
            country_code = city_record[8]
            population = int(city_record[14])
            try:
                elevation = int(city_record[15])
            except ValueError:
                elevation = 0

            cities[city_record[1]] = [population, elevation, country_code]       # key = city name, value = [populuation, elevation]

except IOError as e:
    print('Error: {0}'.format(e))

cities_by_size = sorted(cities, key=sort_by_population, reverse=True)
cities_by_elevation = sorted(cities, key=sort_by_elevation, reverse=True)

largest_city = cities_by_size[0]
largest_population = format_groupings(cities[largest_city][0])
print('Largest city: {0} with: {1} people'.format(largest_city, largest_population))

highest_city = cities_by_elevation[0]
highest_elevation_meters = format_groupings(cities[highest_city][1])
highest_elevation_feet = format_groupings(cities[highest_city][1]*3.28)
print('Highest city: {0} at: {1} meters ({2} feet)'.format(highest_city, highest_elevation_meters, highest_elevation_feet))

# note: to print city names with unicode chars, you'll have to convert to the format supported by the terminal.  Example:
#       encoding = sys.stdout.encoding
#       print(city.encode(encoding, errors='replace').decode(encoding))

city_search = 'city'
while city_search:
    city_search = input('City population search (enter=quit): ')

    if city_search:
        city_search_formatted = ' '.join([word.capitalize() for word in city_search.split()])
        search_population = cities.get(city_search_formatted, [0, 0, ''])[0]
        search_population = format_groupings(search_population) if search_population else 'not found'
        print('City: {0}, population: {1}'.format(city_search_formatted, search_population))
