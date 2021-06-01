# MRO : Method Resolution Order (MRO) is the order in which Python looks
# for a method in a hierarchy of classes. Especially it plays vital role in the context of multiple
# inheritance as single method may be found in multiple super classes.
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1
    # pass


class D(B, C):
    pass


# To check the MRO of a class we can use the following command, this will tell us the way Python will solve it based
# on the hierarchy of classes
# print(D.mro())

# If we print the following method it will show 1
print(D.num)

# The reason is cause the hierarchy is the following:
# D -> B -> C -> A (Instead of be D -> B -> A -> C -> A, the MRO removes one A cause B and C have that Superclass A)
# cause the A of B cant be before C, as C is a superclass of D
# D is inheriting from B and C (Exact order), and then at the end C is inheriting from A as well as B
# but Python found num in C with the value of 1, if we replace num = 1 for pass, then it will go to A
# and then find num = 10 so it will return that value.
