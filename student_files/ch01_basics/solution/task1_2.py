"""

      task1_2.py   -   Python Basics Overview

      Reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

"""
# fixed import statment so pycharm could find it
import os

from city_search import read_city_data, get_highest, get_largest, search

working_dir = '../../resources'
city_data = 'cities15000.txt'

source = os.path.join(working_dir, city_data)
read_city_data(source)

largest_city = get_largest()
highest_city = get_highest()

print(largest_city)
print(highest_city)

print(search('boise'))
print(search('london'))
print(search('whoville'))
