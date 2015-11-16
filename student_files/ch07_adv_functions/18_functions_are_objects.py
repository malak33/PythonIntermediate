def double(val):
    return 2 * val


def triple(val):
    return 3 * val


def compose(val):
    return double(triple(val))

x = 3
if x == 1:
    print(double(5))
elif x == 2:
    print(triple(5))
else:
    print(compose(5))


# ----------------------------------------------------

def double(val):
    return 2 * val


def triple(val):
    return 3 * val


def compose(f1, f2, val):
    return f1(f2(val))

my_funcs = [double, triple, compose]

print(my_funcs[1](5))            # returns 15

# --------------------------------------
import functools


mapped_items = list(map(double, [1, 2, 3]))
print(mapped_items)

filtered_items = list(filter(lambda x: x % 2 == 0, range(1, 15, 3)))
print(filtered_items)

print(functools.reduce(lambda x, y: x+y, [1, 2, 3]))
