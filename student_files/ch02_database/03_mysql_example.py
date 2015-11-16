"""

    03_mysql_example.py

    The following source will create and work with a mysql database table.  It
    assumes MySQL has already been installed by the user.

    Note the user name is assumed to be user1 and the password is assumed to be password.  Change
    this as necessary.

    This example uses the MySQL connector python driver (Oracle driver).

    It creates the schools table and loads it with data.  It tests the table using
    a doctest in the search() function.

"""
import csv
import mysql.connector


data_sourcefile = '../resources/baseball/schools.csv'
DROP_SCHOOLS_SQL = 'DROP TABLE IF EXISTS schools'
CREATE_SCHOOLS_SQL = 'CREATE TABLE IF NOT EXISTS schools (school_id VARCHAR(30) NOT NULL PRIMARY KEY, fullname VARCHAR(250), city VARCHAR(50), state VARCHAR(15), country VARCHAR(50))'
INSERT_RECORD = 'INSERT INTO schools(school_id, fullname, city, state, country) VALUES (%s,%s,%s,%s,%s)'
connect_info = {
    'host': 'localhost',
    'port': 3306,
    'database': 'test',
    'user': 'user1',
    'password': 'password',
    'charset': 'utf8',
    'use_unicode': True,
    'get_warnings': True
}

def load_data(data_sourcefile):
    """ read data from the file into a list of records """
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

    return school_data


def load_db(config):
    results = []
    try:
        db = mysql.connector.Connect(**config)
    except mysql.connector.Error as err:
        results.append('Error connecting to database: {0}'.format(err))
        return results

    cursor = db.cursor()

    try:
        cursor.execute(DROP_SCHOOLS_SQL)                    # Drop table if exists, and create it new
        cursor.execute(CREATE_SCHOOLS_SQL)
    except (mysql.connector.Error, TypeError) as err:
        results.append("Error removing/adding table: {0}".format(err))
        return results
    finally:
        if db:
            db.close()

    try:
        cursor.executemany(INSERT_RECORD, school_data)
        db.commit()
        results.append('Completed reading records.')
    except (mysql.connector.Error, TypeError) as err:
        results.append("Operation Error: {0}".format(err))
    finally:
        if db:
            db.close()

    return results


def search(config, school_name):
    """
        >>> search(connect_info, 'Nevada')
        [('University of Nevada-Reno',), ('College of Southern Nevada',), ('University of Nevada-Las Vegas',)]

        :param config: database connection data
        :param school_name: a school name or partial name to search within the fullname column
        :return: list of tuples containing matching school fullnames
    """
    results = []
    db = None
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor()
        query = 'select fullname from schools where fullname like "%{school_name}%"'.format(school_name=school_name)
        cursor.execute(query)
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        results.append('Error connecting to database: {0}'.format(err))
    finally:
        if db:
            db.close()

    return results


if __name__ == '__main__':
    school_data = load_data(data_sourcefile)
    results = load_db(connect_info)
    print('\n'.join(results))
    test_school_name = 'Nevada'
    import doctest
    doctest.testmod()
