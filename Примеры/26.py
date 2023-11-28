class A:
    def test(self):
        print('A')


class B(A):
    pass


class C:
    def test(self):
        print('C')


class D(B, C):
    pass


d = D()
print(D.__mro__)
