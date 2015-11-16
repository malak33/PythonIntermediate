"""

      task6_2_starter.py   -   Using Generators and Dictionary Comprehensions

      This exercise is a refactoring of the task6_1.py solution.  It
      proposes using a generator to read data from a file
      and a dictionary comprehension to build the country_names dictionary.

        Helpful hints:
        1. Convert the file reading code to a be generator (lines 51-59).
           Here's how:

           The current code builds a list of country codes and
           stores the country code in a list called countries_referenced.
           Modify this code to yield the country code from a function instead (thereby
           creating a generator).

           Build a list of countries_referenced by passing the generator
           into the list's constructor after the function definition, like this:

           countries_referenced = list(read_countries_generator())


        2. In a similar fashion, we'll repeat this for the code that creates
           the dictionary (lines 62-72) this time creating a function that will
           become a generator that yields both the country_code and country_name.
           Instead of storing the values in a dictionary directly, we'll call the
           generator and create the dictionary from the generator using a dictionary comprehension.
           Here's how:

           First, convert the code into a function.  It should yield two values: country_code
           and country_name.
           Call this function as part of a dictionary comprehension to build the dictionary.
           Use the following syntax (change your variables for your code, of course):

            country_names = { key:value for key:value in generator()}

        3. Your new solution should work now, this time with two generators and a dictionary
            comprehension.
"""
import os
from collections import Counter


working_dir = '../resources'
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
