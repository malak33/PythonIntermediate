from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


filename = 'harry.jpg'
host = 'localhost'
port = 8053


def get_file():
    with open(filename, 'rb') as f:
        return xmlrpc.client.Binary(f.read())


server = SimpleXMLRPCServer((host, port))
print('{host} running on {port}...'.format(host=host, port=port))
server.register_function(get_file, 'get_file')
server.serve_forever()
