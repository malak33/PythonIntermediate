def func1(greeting):
    print(greeting)


def count(orig_func):
    class Count:
        calls = 0
    def wrapper(*args, **kwargs):
        Count.calls += 1
        print('{fname}, call #{num_calls}'.format(fname=orig_func.__name__, num_calls=Count.calls))
        return orig_func(*args, **kwargs)
    return wrapper

func1 = count(func1)
func1('hello')
func1(greeting='howdy')

