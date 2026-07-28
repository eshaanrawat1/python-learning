# python supports multiple inheritance through MRO 
# MRO (method resolution order) defines a hierarchy of 
# where to look for calling a method (starting in the current class
# and moving through the chain via super)
#
# this means methods can be defined in multiple classes
# however MRO is not always valid (case below)


# object
#   |
#   A
#  /  \
# B    C
#  \  /
#   D

class A:
    def foo(self):
        print('A')

class B(A):
    def foo(self):
        print('B')

class C(A):
    def foo(self):
        print('C')

class D(B, C):
    def bar(self):
        print('d bar')

D().foo()
# B

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# this means we look to D -> B -> C -> A -> object

# class X(B, C):
#     pass

# class Y(C, B):
#     pass

# class Z(X, Y):
#     pass

# Traceback (most recent call last):
#   File "multiple_inheritance.py", line 47, in <module>
#     class Z(X, Y):
#         pass
# TypeError: Cannot create a consistent method resolution order (MRO) 
# for bases B, C
#
# this fails since X requires B before C but Y requires C before B


class X:
    def bar(self):
        print('x')

class Y(X):
    def bar(self):
        print('y')
        super().bar()

class Z(Y):
    def bar(self):
        print('z')
        super().bar()

Z().bar()
# z
# y
# x
# super continues each step in the mro


# class E(int, str):
#     pass
# Traceback (most recent call last):
#   File "/multiple_inheritance.py", line 81, in <module>
#     class E(int, str):
#         pass
# TypeError: multiple bases have instance lay-out conflict
# incompatible memory layouts between int and str