"""

      task6_2.py   -   Using Generators and Dictionary Comprehensions

      This exercise is a refactoring of the task6_1.py solution.  It
      proposes using a generator to read data from a file
      and a dictionary comprehension to build the country_names dictionary.
"""
import os
from collections import Counter


working_dir = '../../resources'
city_data = 'cities15000.txt'
country_info = 'countryInfo.txt'


def read_countries_generator():
    try:
        with open(os.path.join(working_dir, city_data), encoding='utf8') as cities_file:
            for line in cities_file:
                city_record = line.strip().split('\t')
                country_code = city_record[8]
                yield country_code
    except IOError as e:
        print('Error: {0}'.format(e))


def read_country_names_generator():
    try:
        with open(os.path.join(working_dir, country_info), encoding='utf8') as countries_file:
            for idx, line in enumerate(countries_file):
                if idx > 50:
                    country_record = line.strip().split('\t')
                    country_code = country_record[0]
                    country_name = country_record[4]
                    yield country_code, country_name
    except IOError as e:
        print('Error: {0}'.format(e))


countries_referenced = list(read_countries_generator())
country_names = { code:name for code, name in read_country_names_generator()}

# calculate the country with the most cities over 15000
most_common_countries = Counter(countries_referenced).most_common(2)
most_common, count = most_common_countries[0]
second_most_common, second_count = most_common_countries[1]

print('Country with most cities over 15000 population: {0} with {1} cities.'
      .format(country_names[most_common], count))
print('Country with second most cities over 15000 population: {0} with {1} cities.'
      .format(country_names[second_most_common], second_count))
