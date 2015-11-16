"""
    Demonstrates the use of wraps, from functools.
    Run this, then remove the wraps inner decorator and run again.
    Note the difference.
"""

from functools import wraps

def dec(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        return f(*args, **kwds)
    return wrapper

@dec
def my_func():
    """
        Using wraps in the decorator preserves this string
        and the function name
    """
    print(my_func.__name__)
    print(my_func.__doc__)

my_func()