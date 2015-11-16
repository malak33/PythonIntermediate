"""
      task2_1.py   -   Python Database API 2.0

      Reads data from school.db by providing a get_location() function and a partial or full
      name of a school.

      Data returned from the search of the database returns name, city, and state for all
      matching results.

      Uses a named tuple to store school data.

"""
import sqlite3
from collections import namedtuple

School = namedtuple('School', 'name city state')

data_sourcefile = '../schools.db'
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
