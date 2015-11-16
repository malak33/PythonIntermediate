import collections
import csv
from xmlrpc.server import SimpleXMLRPCServer


filename = '../resources/airports.dat'
host = 'localhost'
port = 8052


def get_airport(abbr):
    results = 'not found'
    try:
        with open(filename, encoding='utf8') as f:
            try:
                headings = f.readline().strip()[1:].split(',')                      # [1:] is stripping the \ufeff byte order mark out.
                tuple_attributes = ' '.join([heading.strip() for heading in headings])
                Airport = collections.namedtuple('Airport', tuple_attributes)
                for row in csv.reader(f):
                    airport = Airport(*row)
                    if abbr.upper() in airport.IATA_FAA:
                        results = '{name} ({city}, {country}) Abbr: {IATA_FAA}'.format(**airport.__dict__)
            except csv.Error as e:
                print('Error: {err}'.format(err=e))
    except IOError as err:
        print('Error with {fn}: {err}'.format(fn=filename, err=err))

    return results


server = SimpleXMLRPCServer((host, port))
print('{host} running on {port}...'.format(host=host, port=port))
server.register_function(get_airport, 'search_airport')
server.serve_forever()
