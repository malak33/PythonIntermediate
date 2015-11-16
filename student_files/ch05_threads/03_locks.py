import time
from threading import Thread, Lock

class Worker(Thread):
    lock = Lock()
    def __init__(self, name, sleeptime):
        Thread.__init__(self, name=name)
        self.sleeptime = sleeptime
    
    def run(self):
        Worker.lock.acquire()
        shared_resource(self.name, self.sleeptime)
        Worker.lock.release()

def shared_resource(name, sleeptime):
    print('{0} in shared_resource'.format(name))
    time.sleep(sleeptime)
    print('{0} leaving shared_resource'.format(name))

def main():
    th1 = Worker('Thr1', 4)
    th2 = Worker('Thr2', 2)
    th1.start()
    th2.start()

if __name__ =='__main__':
    main()
