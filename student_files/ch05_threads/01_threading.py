from threading import Thread

class Worker(Thread):
    def __init__(self, name='CountThread'):
        Thread.__init__(self, name=name)

    def run(self):
        print('This is {0}'.format(self.name))

def main():
    m = Worker('Worker')
    m.start()

if __name__ =='__main__':
    main()