def dec1(f):
    def wrapper(*args, **kwargs):
        print('dec1')
        return f(*args, **kwargs)
    return wrapper

def dec2(f):
    def wrapper(*args, **kwargs):
        print('dec2')
        return f(*args, **kwargs)
    return wrapper

@dec1
@dec2
def my_func():
    print('This is my function')

my_func()