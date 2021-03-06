"""
      task7_1_starter.py   -   Using the logging Module

      The program reads data from school.db by providing a
      partial or full name of a school.

      Data returned from the search of the database
      returns name, city, and state for all matching results.

      Uses a named tuple to store school data.  This exercise uses
      another module (logging.py) to configure and set up a logger.
      The logger will be implemented as a decorator and used to
      decorate the get_location() method of the starter file.

      Helpful hints:

      1. Refer to logger.py in the starter/support folder on
         how to configure/create the logger.

      2. Add the import for logger.py and the decorator above the method
         in this module.

"""
import sqlite3
from collections import namedtuple


School = namedtuple('School', 'name city state')

data_sourcefile = '../../ch02_database/schools.db'
SELECT_SCHOOLS_SQL = 'SELECT fullname, city, state FROM schools WHERE fullname like "%{0}%"'


def get_location(school_name):
    school_data = []
    connection = None

    try:
        connection = sqlite3.connect(data_sourcefile)
    except sqlite3.Error as err:
        print('Error connecting to database: {0}'.format(err))
        return school_data

    connection.row_factory = sqlite3.Row                             # allows accessing cursor record by column name instead of index value
    cursor = connection.cursor()

    try:
        cursor.execute(SELECT_SCHOOLS_SQL.format(school_name))
        for sch in cursor.fetchall():
            school_data.append(School(*sch))
    except sqlite3.Error as e:
        print('Error processing request: {0}'.format(e))
        return school_data
    finally:
        if connection:
            connection.close()
    return school_data


name = input('School name (or partial name): ')
results = get_location(name)
print('Matches for {0}:'.format(name))
for school in results:
    print('{name}, {city} {state}'.format(**school.__dict__))
