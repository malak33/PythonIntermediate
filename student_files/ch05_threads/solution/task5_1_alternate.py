"""
        task5_1_alternate.py  -   Multi-threaded Pinger

        This version uses thread.join() to wait for all results to come back
        before working with (displaying) the results
"""

from subprocess import Popen, PIPE
from threading import Thread
class Pinger(Thread):
    def __init__(self, address):
        Thread.__init__(self)
        self.address = address
        self.results = None
        self.err_msg = None

    def run(self):
        p = Popen(['ping', self.address], stdout=PIPE)
        print('Pinging host: {host}'.format(host=self.address))
        self.results, self.err_msg = p.communicate(None)


all_threads = []
addresses = 'www.google.com', 'www.yahoo.com', 'www.im_a_fake_address.com'
for addr in addresses:
    pinger_thread = Pinger(addr)
    pinger_thread.start()
    all_threads.append(pinger_thread)

for thr in all_threads:                 # don't show the results until all threads have concluded
    thr.join()

for thr in all_threads:
    print('Results for: {0}: {1}'.format(thr.address, thr.results.decode()))