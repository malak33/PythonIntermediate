"""

    01_create_schools_db_using_with.py

    The following source will create (and destroy any previous) tables related
    to the school data loaded from schools.csv.

    At any time this file can be run to re-establish a fresh version of the
    database.  It should create a database file called schools.db.

"""
import csv
import sqlite3

data_sourcefile = '../resources/baseball/schools.csv'
DROP_SCHOOLS_SQL = 'DROP TABLE IF EXISTS schools'
CREATE_SCHOOLS_SQL = 'CREATE TABLE IF NOT EXISTS schools (school_id VARCHAR(30) NOT NULL PRIMARY KEY, fullname VARCHAR(50), city VARCHAR(50), state VARCHAR(15), country VARCHAR(50))'
INSERT_RECORD = 'INSERT INTO schools(school_id, fullname, city, state, country) VALUES (?,?,?,?,?)'


# read data from the file into a list of records
school_data = []
try:
    with open(data_sourcefile, encoding='utf8') as f:
        try:
            for row in csv.reader(f):
                school_data.append(row)
        except csv.Error as e:
            print('Error: {err}'.format(err=e))
except IOError as e:
    print(e)


school_data = school_data[1:]
connection = None
try:
    with sqlite3.connect('schools.db') as connection:
        cursor = connection.cursor()
        cursor.execute(DROP_SCHOOLS_SQL)
        cursor.execute(CREATE_SCHOOLS_SQL)
        cursor.executemany(INSERT_RECORD, school_data)
        print('Data loaded into schools table')
except sqlite3.Error as e:
    print('Data not loaded into schools table')
    print('Error: {0}'.format(e))
finally:
    if connection:
        connection.close()