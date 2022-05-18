# MRO : Method Resolution Order (MRO) is the order in which Python looks
# for a method in a hierarchy of classes. Especially it plays vital role in the context of multiple
# inheritance as single method may be found in multiple super classes.


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
