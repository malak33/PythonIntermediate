"""
    task8_1.py  -   This task will implement the retrieve() method of the DocumentManager
                    class and add a unit test to verify its return value.


    Usage:
        task8_1.py -add <path_to_file>/filename
        or
        task8_1.py -remove filename


    This file is a continuation of an earlier exercise (task6_2.py).

    This version implements the retrieve() method of the DocumentManager.  It then
    creates a unit test to test it.

    Note: for imports to work properly, your student_files folder should be on your
    PYTHONPATH.

    Also, remember to run server.py before running this client.
"""
import argparse
import pprint
import sys
from queue import Queue
from threading import Thread

import ch08_testing.solution.client as client


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
