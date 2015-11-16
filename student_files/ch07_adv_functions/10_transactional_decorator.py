class Transactional(object):
    @staticmethod
    def tx(f):
        def wrapper(self, *args, **kwargs):
            ret=None
            self.session.begin()
            try:
                ret = f(self, *args, **kwargs)
                self.session.commit()
            except Exception:
                self.session.rollback()

            return ret
        return wrapper
        
    def __init__(self, session):
        self.session = session


class Work(Transactional):
    def __init__(self, session):
        super().__init__(session)
        
    @Transactional.tx
    def work(self):
        print('do work')
    
    @Transactional.tx
    def more_work(self):
        print('do more work')
        raise Exception                     #purposely causes an exception


class SessionStub:
    """
        Simulates a database session
    """
    def begin(self):
        print('begin')

    def commit(self):
        print('commit')

    def rollback(self):
        print('rollback')


m = Work(SessionStub())
m.work()
m.more_work()               # generates an exception, and thus a rollback
