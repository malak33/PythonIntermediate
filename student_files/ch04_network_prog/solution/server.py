import os
from xmlrpc.server import SimpleXMLRPCServer

from globals import host, port
from document import DocumentManager


server_document_location = '../../user_documents'


def receive_file(filename, results, is_public=False):
    file_location = os.path.join(server_document_location, filename)
    with open(file_location, 'wb') as f:
        f.write(results.data)

    return DocumentManager().add(filename, filesize=os.stat(file_location).st_size, is_public=is_public)


def list_public():
    return DocumentManager().list_public()


server = SimpleXMLRPCServer((host, port), allow_none=True)
print('{host} running on {port}...'.format(host=host, port=port))
print('Archive directory: {archive_location}'.format(archive_location=os.path.abspath(server_document_location)))
server.register_function(receive_file, 'upload')
server.register_function(list_public)
server.serve_forever()
