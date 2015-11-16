class dec:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print('do stuff first')
        retval = self.func(*args)
        print('do stuff last')
        return retval


@dec
def foo(val):
    return val

# foo = dec(foo)

print(foo(5))
print(foo('hello'))