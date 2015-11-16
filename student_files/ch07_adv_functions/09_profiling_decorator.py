import time

def profile(orig_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = orig_func(*args, **kwargs)
        finish = time.time()
        print('{fname} took {delta:.2f}sec'.format(fname=orig_func.__name__, delta=(finish - start)))
        return ret
    return wrapper


@profile
def func1(greeting, farewell):
    print(greeting)
    time.sleep(3)
    print(farewell)
    
func1('hello', farewell='goodbye')