import os
import re
from xmlrpc.server import SimpleXMLRPCServer

from ch05_threads.solution2.globals import host, port
from ch05_threads.solution2.document import DocumentManager


server_document_location = '../../user_documents'


def receive_file(filename, results, is_public=False):
    file_location = os.path.join(server_document_location, filename)

    # if file exists, this adds a "_nn" onto the end of the filename
    count = 0
    while os.path.isfile(file_location):
        fn, ext = os.path.splitext(filename)
        fn = re.sub('_\d$', '', fn)
        filename = fn + '_' + str(count) + ext
        file_location = os.path.join(server_document_location, filename)
        count += 1

    with open(file_location, 'wb') as f:
        f.write(results.data)

    return DocumentManager().add(filename, filesize=os.stat(file_location).st_size, is_public=is_public)


def list_public():
    return DocumentManager().list_public()


def remove(filename):
    file_location = os.path.join(server_document_location, filename)
    db_remove_results = False
    try:
        db_remove_results = DocumentManager().remove(filename)
        os.remove(file_location)
    except OSError:
        pass

    return db_remove_results


server = SimpleXMLRPCServer((host, port), allow_none=True)
print('{host} running on {port}...'.format(host=host, port=port))
print('Archive directory: {archive_location}'.format(archive_location=os.path.abspath(server_document_location)))
server.register_function(receive_file, 'upload')
server.register_function(list_public)
server.register_function(remove)
server.serve_forever()
