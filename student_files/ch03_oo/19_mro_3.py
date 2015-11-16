class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        super().__init__()
        print('B')


class C(A):
    def __init__(self):
        super().__init__()
        print('C')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('D')


class E(B, C):
    def __init__(self):
        super().__init__()
        print('D')


class F(D, E):
    def __init__(self):
        super().__init__()
        print('D')

f = F()
print(F.mro())