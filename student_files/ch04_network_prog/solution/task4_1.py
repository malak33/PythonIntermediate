"""
    task4_1.py  -   document listing test file

    This file is a continuation of the previous exercise (task3_1.py).

    In this part of the exercise, the driver will communicate with a new module.  This
    module contains a DocumentXMLRPC client and server.

    Note: for imports to work properly, your student_files folder should be on your
    PYTHONPATH.

    Also, remember to run server.py before running this client.
"""

import ch04_network_prog.solution.client as client


file_to_send = '../harry.jpg'


def upload(filename):
    client.send_file(filename, True)
    public_files = client.list_public()

    return public_files


print(upload(file_to_send))
