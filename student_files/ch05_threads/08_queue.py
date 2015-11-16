from queue import Queue
from threading import Thread


num_worker_threads = 5


def do_work1():
    print('work1 function')


def do_work2():
    print('work2 function')


def do_work3():
    print('work3 function')

tasks = [do_work1, do_work2, do_work3]

q = Queue()
for item in tasks:
    q.put(item)


class WorkerThread(Thread):
    def run(self):
        while True:
            work = q.get()
            work()
            q.task_done()

for i in range(num_worker_threads):
     t = WorkerThread()
     t.daemon = True
     t.start()


q.join()       # don't end main thread until all tasks are finished