import os
import time

from multiprocessing import Process, freeze_support

def work():
    print('work process id: {0}'.format(os.getpid()))
    time.sleep(10)

if __name__ == '__main__':
    freeze_support()
    print('Main pid: {0}'.format(os.getpid()))
    Process(target=work).start()
    Process(target=work).start()
    Process(target=work).start()
