"""
    task5_2.py  -   Modified document archive client that can add (upload) or remove (delete) files


    Usage:
        task5_2.py -add <path_to_file>/filename
        or
        task5_2.py -remove filename


    This file is a continuation of an earlier exercise (task4_2.py).

    This part of the exercise is optional.  It adds a remove() feature to the DocumentManager
    and to the client and server for the XMLRPC exchange.

    This version also handles duplicate "add" calls.

    Note: for imports to work properly, your student_files folder should be on your
    PYTHONPATH.

    Also, remember to run server.py before running this client.
"""
import sys
from queue import Queue
from threading import Thread


import ch05_threads.solution2.client as client

if len(sys.argv) != 3:
    print('Improper usage. Syntax: python task5_2_starter.py [-add <path>/filename][-remove filename]')
    sys.exit(42)


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
            print(results)
            output_queue.task_done()


if sys.argv[1] == '-add':
    file_to_send = sys.argv[2]
    task = [client.send_file, (file_to_send, True)]
    q.put(task)

elif sys.argv[1] == '-remove':
    file_to_remove = sys.argv[2]
    task = [client.remove, (file_to_remove,)]
    q.put(task)


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
