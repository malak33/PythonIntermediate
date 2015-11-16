"""
    task5_2_starter.py  -   Using Queues to process tasks


    Usage:
        task5_2_starter.py -add <path_to_file>/filename
        or
        task5_2_starter.py -remove filename


    This file is a continuation of an earlier exercise (task4_2.py).

    Complete only this file to implement a Queue that will perform the task of invoking
    the client.  Follow the specific instructions below...

    Note: for imports to work properly, your student_files folder should be on your
    PYTHONPATH.

    Also, remember to run server.py before running this client.


    Instructions
    ------------
    1. Create a Queue (after the code that checks for proper arguments).

    2. Create a class that will perform work.  This class will pull a task from the queue
       and invoke that task.  Since tasks are basically functions, the functions may have
       arguments as well.  We will need to add the arguments to the function also.  Create
       the following class that will read the task to perform and arguments to pass into the task:

       class WorkerThread(Thread):
           def run(self):
               while True:
                   work, args = q.get()
                   results = work(*args)
                   output_queue.put(results)
                   q.task_done()


    3. Anywhere we invoke the client.py client methods, we will need to modify the code.  Instead
       of directly invoking the client, like this:

                client.send_file(file_to_send, True)

       Now, we will queue the task up, and let a thread invoke it, like this:

                    task = [client.send_file, (file_to_send, True)]
                    q.put(task)

       Notice the task is broken into the function name and then the arguments.  This is what
       we will store in the queue.

       Can you complete the queueing of the other two tasks (client.remove and client.list_public() ) on your own?

    4. Displaying return values from the RPC calls is trickier now since the return values
       will be acquired from within a thread.  One option is to queue the return values
       up in a 2nd queue and simply display the values.

       Beneath your WorkerThread class, create a second queue and a thread class to process that
       queue...

                    output_queue = Queue()

                    class ResultsThread(Thread):
                        def run(self):
                            while True:
                                results = output_queue.get()
                                print(results)
                                output_queue.task_done()


    5. Finally, at the bottom of your code, create a pool of threads to process the work queue.
       Also, process the output queue.  Finally, ensure the main program doesn't end until all
       queue tasks have been processed.  The following code should do this for you:

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

"""

import sys

import ch05_threads.starter.client as client

if len(sys.argv) != 3:
    print('Improper usage. Syntax: python task5_2_starter.py [-add <path>/filename][-remove filename]')
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
