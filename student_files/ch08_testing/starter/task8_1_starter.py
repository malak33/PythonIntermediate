"""
    task8_1_starter.py  -   This task will implement the retrieve() method of the DocumentManager
                            class and add a unit test to verify its return value.


    Usage:
        task8_1_starter.py -add <path_to_file>/filename
        or
        task8_1_starter.py -remove filename


    This file is a continuation of an earlier exercise (task6_2.py).

    This version implements the retrieve() method of the DocumentManager.  It then
    creates a unit test to test it.

    Note: for imports to work properly, your student_files folder should be on your
    PYTHONPATH.

    Also, remember to run server.py before running this client.


    Instructions:
    -------------
    1. Locate starter/document.py.  Complete the retrieve() method.  It
       should query the database and return a Document object when a filename is passed in.

        Hints:
                a) Execute a cursor with the following SQL:
                    'SELECT * FROM {tbl} WHERE {column}="{value}"'.format(tbl='documents', column='filename', value=filename)
                b) fetchone() record from the cursor
                c) instantiate a Document type object, populate it and return it from the function
                        Document(doc['filename'], doc['path'], doc['is_public'], doc['filesize'], doc['when_added'])
                    where doc is the result of the fetchone() operation


    2. To test your newly created method, open starter/tests/test_document.py.  Within this file,
       a unit test has been started for you.  Complete the class by making a test_______() method
       which checks if a proper Document object was returned.

        Hints:

                a) Create a setup() method that instantiates a DocumentManager() object
                   (pass in the provided db_file location to override the default).  Attach the
                   DocumentManager to the self reference so that it remains available for the test________()
                   method.

                b) In the test method, a possible input value could be 'sample.txt' which
                   should return the following document object:

                        Document('sample.txt', '', 1, 70, 'May 18 2015 04:34PM')

                   Check that a proper Document object is returned.


    3. Run the unit test to verify the retrieve() method works as expected.
"""
import argparse
import pprint
import sys
from queue import Queue
from threading import Thread

import ch08_testing.starter.client as client


parser = argparse.ArgumentParser(description='Personal characteristics')
mutual_group = parser.add_mutually_exclusive_group()
mutual_group.add_argument('-add')
mutual_group.add_argument('-remove')
args = parser.parse_args()

q = Queue()


class WorkerThread(Thread):
    def run(self):
        while True:
            work, args = q.get()
            results = work(*args)
            output_queue.put(results)
            q.task_done()


output_queue = Queue()


class ResultsThread(Thread):
    def run(self):
        while True:
            results = output_queue.get()
            pprint.pprint(results, width=1, indent=2)
            output_queue.task_done()


# optionally move this into a function
if args.add:
    file_to_send = args.add
    task = [client.send_file, (file_to_send, True)]
    q.put(task)

elif args.remove:
    file_to_remove = args.remove
    task = [client.remove, (file_to_remove,)]
    q.put(task)
else:
    sys.exit(42)


task = [client.list_public, ()]
q.put(task)

num_worker_threads = 5
for i in range(num_worker_threads):
    t = WorkerThread()
    t.daemon = True
    t.start()


q.join()                        # don't end main thread until all tasks are finished

results_thread = ResultsThread()
results_thread.daemon = True
results_thread.start()
output_queue.join()
