"""

      city_search.py   -   Refactored task1_1.py solution, used with task1_2 module (exercise)

      Reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

"""
import locale

cities = {}
locale.setlocale(locale.LC_ALL, '')


def _format_groupings(value):
    return locale.format('%d', value, grouping=True)


def read_city_data(data_source='../../resources/cities15000.txt'):
    try:
        with open(data_source, encoding='utf8') as cities_file:
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


def search(city_search):
    default_record = [0, 0, '']

    if city_search:
        city_search_formatted = ' '.join([word.capitalize() for word in city_search.split()])
        search_population = cities.get(city_search_formatted, default_record)[0]
        search_population = _format_groupings(search_population) if search_population else 'not found'
        return 'City: {0}, population: {1}'.format(city_search_formatted, search_population)


def get_largest():
    sort_by_population = lambda k: cities[k][0]
    cities_by_size = sorted(cities, key=sort_by_population, reverse=True)
    largest_city = cities_by_size[0]
    largest_population = _format_groupings(cities[largest_city][0])
    return 'Largest city: {0} with: {1} people'.format(largest_city, largest_population)


def get_highest():
    sort_by_elevation = lambda k: cities[k][1]
    cities_by_elevation = sorted(cities, key=sort_by_elevation, reverse=True)
    highest_city = cities_by_elevation[0]
    highest_elevation_meters = _format_groupings(cities[highest_city][1])
    highest_elevation_feet = _format_groupings(cities[highest_city][1]*3.28)
    return 'Highest city: {0} at: {1} meters ({2} feet)'.format(highest_city, highest_elevation_meters, highest_elevation_feet)

# note: to print city names with unicode chars, you'll have to convert to the format supported by the terminal.  Example:
#       encoding = sys.stdout.encoding
#       print(city.encode(encoding, errors='replace').decode(encoding))
