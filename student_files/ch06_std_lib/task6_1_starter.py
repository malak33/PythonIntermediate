"""

      task6_1_starter.py   -   Determining the country with the most cities with more than
                               15000 people.  Read cities15000.txt.

      This is a revised version of task1_1.py.  This version

"""
import os


working_dir = '../resources'
city_data = 'cities15000.txt'
country_info = 'countryInfo.txt'
countries_referenced = []
country_names = {}

# read cities15000.txt, store country codes in a list
try:
    with open(os.path.join(working_dir, city_data), encoding='utf8') as cities_file:
        for line in cities_file:
            pass # remove this 'pass' line when you begin working

            # Step 1. Place country code (two-digit country abbreviations)
            # (country_code is the eighth column of data) into the provided list of countries

except IOError as e:
    print('Error: {0}'.format(e))


# read countryInfo.txt, skip the first 51 lines, store country names and codes in a dictionary
try:
    with open(os.path.join(working_dir, country_info), encoding='utf8') as countries_file:
        pass # remove this 'pass' line when you begin working

        # Step 2. Iterate over the lines from the countryInfo.txt file,
        #         extract the country code (first column) AND the full country name (fifth column).
        #         Put them into the provided dictionary.
        #         Note: watch this file!--the first 51 lines should be skipped!

except IOError as e:
    print('Error: {0}'.format(e))


# calculate the country with the most cities over 15000

# Step 3. Use the collection module's Counter class to find the most common country in the list.
#         Use that value to determine the full name of the country.
#         Display your result.  Can you get the second country with the most cities over 15000?
