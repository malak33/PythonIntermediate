def dec_args(mask=None, allcaps=False):
    def wrapper_outer(f):
        def wrapper(*args):
            if allcaps:
                args = tuple([arg.upper() for arg in args])
            if mask:
                args = (args[0], '****') + args[2:]

            retval = f(*args)
            print('do stuff after...')
            return retval
        return wrapper
    return wrapper_outer


@dec_args(True, allcaps=True)
def my_func(first, last):
    print('{fn} {ln}'.format(fn=first, ln=last))

my_func('Bill', 'Smith')