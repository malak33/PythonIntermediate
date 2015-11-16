class dec_args:
    """
        supports two arguments: mask - masks the last name,
                                allcaps keyword - displays lastname
    """

    def __init__(self, mask=None, allcaps=False):
        self.mask = mask
        self.allcaps = allcaps

    def __call__(self, f):
        def wrapper(*args):
            if self.allcaps:
                args = tuple([arg.upper() for arg in args])
            if self.mask:
                args = (args[0], '****') + args[2:]

            retval = f(*args)
            print('do stuff after if desired...')
            return retval
        return wrapper


@dec_args(True, allcaps=True)
def my_func(first, last):
    print('{fn} {ln}'.format(fn=first, ln=last))


@dec_args(False, allcaps=False)
def my_func2(first, last):
    print('{fn} {ln}'.format(fn=first, ln=last))

my_func('Bill', 'Smith')
my_func2('Bill', 'Smith')
