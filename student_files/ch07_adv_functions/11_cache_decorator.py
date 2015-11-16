def cache_decorator(orig_func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            print('using cache for...{0}'.format(args))
        else:
            ret = orig_func(*args)
            cache[args] = ret
        return cache[args]
    
    return wrapper


@cache_decorator
def orig_func(*args):
    print('Executing {0} using {1}'.format(orig_func.__name__, args))


orig_func(1)
orig_func(1,2,3)
orig_func('hello')
orig_func(1)
orig_func('hello')
orig_func(1,2)












