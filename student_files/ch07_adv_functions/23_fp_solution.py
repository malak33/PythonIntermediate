double = lambda val: 2*val
triple = lambda val: 3*val
compose = lambda f1, f2, val: f1(f2(val))

newFunc = lambda x, y: (x == 1 and double(y)) or (x == 2 and triple(y)) or (compose(double, triple, y))

mapobj = map(newFunc, range(1, 4), [5]*3)
print('\n'.join([str(i) for i in mapobj]))