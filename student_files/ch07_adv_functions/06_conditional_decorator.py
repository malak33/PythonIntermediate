def conditional_execute(some_func):
    def modified(name):
        retval = None
        print ('(before method executes)')
        if name.lower() != 'rob':
            retval = some_func(name)
        else:
            print('Skipping execution of {0}'.format(some_func.__name__))
        print('(after method executes)')
        return retval
    return modified

@conditional_execute
def orig_func(name):
    print('Hello {0}'.format(name))

orig_func('Bob')
orig_func('Rob')