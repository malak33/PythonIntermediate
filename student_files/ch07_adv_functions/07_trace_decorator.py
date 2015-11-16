def trace(orig_func):
    def wrapper(*args, **kwargs):
        print('Calling: {fname}...'.format(fname=orig_func.__name__))
        return orig_func(*args, **kwargs)
    return wrapper

@trace
def func2(val):
    print(val)

@trace
def func1(val):
    func2(val)

func1(val='hello')


