import inspect

def my_func(a, b=1, c=2, *d, e, f=3, **g) -> list:
    frame = inspect.currentframe()
    args, varargs, varkwargs, locals = inspect.getargvalues(frame)
    args.extend(varargs)
    args.extend(varkwargs)
    return [(i, locals[i]) for i in args]

results = my_func(10, 20, e=40, x=50)

print(results)
