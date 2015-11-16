def double(val):
    return 2*val


def triple(val):
    return 3*val


def compose(f1, f2, val):
    return f1(f2(val))

testValues = [1, 2, 3]
y = 5
for x in testValues:
    if x == 1:
        print(double(y))
    elif x == 2:
        print(triple(y))
    else:
        print(compose(double, triple, y))
