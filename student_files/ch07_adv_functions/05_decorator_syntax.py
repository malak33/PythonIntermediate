# the decorator pattern


def decorator(some_func):
    def modified(name):
        print('I have been enhanced.')
        return some_func(name)
    return modified

@decorator
def orig_func(name):
    print('Hello {0}'.format(name))

orig_func('Bob')