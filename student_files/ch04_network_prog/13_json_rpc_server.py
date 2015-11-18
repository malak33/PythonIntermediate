"""

        13_json_rpc_server.py  -

            This server uses JSON-RPC receive requests.  A sample
            client can be found in 14_json_rpc_client.py.

            To run this, you should install two small dependencies:

                pip install Werkzeug

                pip install json-rpc.

            Run this first, then run 14_json_rpc_client.py

"""
import sqlite3
from collections import namedtuple

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

School = namedtuple('School', 'name city state')
data_sourcefile = '../ch02_database/schools.db'
SELECT_SCHOOLS_SQL = 'SELECT fullname, city, state FROM schools WHERE fullname like "%{0}%"'


@dispatcher.add_method
def get_location(school_name):
    school_data = []
    connection = None

    try:
        connection = sqlite3.connect(data_sourcefile)
        print('here!')
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


@Request.application
def application(request):
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


run_simple('localhost', 8005, application)
