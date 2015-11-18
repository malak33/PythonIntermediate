"""
        task5_1.py  -   Multi-threaded Pinger

        The multi-threaded pinger is a class that inherits from Thread,
        passes addresses into its constructor, and ping's them at the operating
        system level by creating a subprocess for each address in the thread's run() method.
"""
from subprocess import Popen, PIPE
from threading import Thread


class Pinger(Thread):
    def __init__(self, address):
        Thread.__init__(self)
        self.address = address

    def run(self):
        p = Popen(['ping', self.address], stdout=PIPE)
        print('Pinging host: {host}'.format(host=self.address))
        results, err = p.communicate(None)
        print('Results: {0}'.format(results.decode()))

addresses = 'www.google.com', 'www.yahoo.com', 'www.theverge.com'
for addr in addresses:
    Pinger(addr).start()