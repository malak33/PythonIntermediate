"""
    task4_2.py  -   Modified document archive client that can add (upload) or remove (delete) files


    Usage:
        task4_2.py -add <path_to_file>/filename
        or
        task4_2.py -remove filename


    This file is a continuation of the previous exercise (task4_1.py).

    This part of the exercise is optional.  It adds a remove() feature to the DocumentManager
    and to the client and server for the XMLRPC exchange.

    This version also handles duplicate "add" calls.

    Note: for imports to work properly, your student_files folder should be on your
    PYTHONPATH.

    Also, remember to run server.py before running this client.
"""
import sys

import ch04_network_prog.solution2.client as client

if len(sys.argv) != 3:
    print('Improper usage. Syntax: python task4_2_starter.py [-add <path>/filename][-remove filename]')
    sys.exit(42)

if sys.argv[1] == '-add':
    file_to_send = sys.argv[2]
    client.send_file(file_to_send, True)
elif sys.argv[1] == '-remove':
    file_to_remove = sys.argv[2]
    is_removed = client.remove(file_to_remove)
    if is_removed:
        print('{fn} removed.'.format(fn=file_to_remove))


files = client.list_public()
print(files)
