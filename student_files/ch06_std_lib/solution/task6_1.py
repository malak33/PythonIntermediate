"""

      task6_1.py   -           Determining the country with the most cities with more than
                               15000 people.  Read cities15000.txt.

      This is a revised version of task1_1.py.

"""
import os
from collections import Counter

working_dir = '../../resources'
city_data = 'cities15000.txt'
country_info = 'countryInfo.txt'
countries_referenced = []
country_names = {}

# read cities15000.txt, store country codes in a list
try:
    with open(os.path.join(working_dir, city_data), encoding='utf8') as cities_file:
        for line in cities_file:
            city_record = line.strip().split('\t')
            country_code = city_record[8]
            countries_referenced.append(country_code)
except IOError as e:
    print('Error: {0}'.format(e))


# read countryInfo.txt, skip the first 51 lines, store country names and codes in a dictionary
try:
    with open(os.path.join(working_dir, country_info), encoding='utf8') as countries_file:
        for idx, line in enumerate(countries_file):
            if idx > 50:
                country_record = line.strip().split('\t')
                country_code = country_record[0]
                country_name = country_record[4]
                country_names[country_code] = country_name
except IOError as e:
    print('Error: {0}'.format(e))


# calculate the country with the most cities over 15000
most_common_countries = Counter(countries_referenced).most_common(2)
most_common, count = most_common_countries[0]
second_most_common, second_count = most_common_countries[1]

print('Country with most cities over 15000 population: {0} with {1} cities.'
      .format(country_names[most_common], count))
print('Country with second most cities over 15000 population: {0} with {1} cities.'
      .format(country_names[second_most_common], second_count))
