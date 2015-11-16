"""

      task6_3_starter.py   -   Using the argparse Module

      This exercise is a refactoring of the task6_2.py solution.  It
      proposes parsing command-line arguments to determine how many results to display.
      The following command line arguments shall be used:

        python task6_3_starter.py -c 5

		    or

        python task6_3_starter.py --count 5


      Helpful hints:

      1. Create a function called get_args() that instantiates the argparse
         parser and adds the -c and --count argument.  Return the parsed args
         from this function.

      2. Invoke the function, retrieving the parsed command-line arguments from
         the argparse parser.

      3. Use the args.count property in a loop to display the most common countries


"""
import os
from collections import Counter


working_dir = '../resources'
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
