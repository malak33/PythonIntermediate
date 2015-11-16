# the decorator pattern


def decorator(some_func):
    def modified(name):
        print('I have been enhanced.')
        return some_func(name)
    return modified


def orig_func(name):
    print('Hello {0}'.format(name))

orig_func = decorator(orig_func)

orig_func('Bob')