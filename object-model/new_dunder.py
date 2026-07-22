# the __new__ dunder is the actual constructor for a class
# __init__ is responsible for initializing attributes 
# __new__ allocates memory for an object and returns it

class A:
    def __new__(cls, *args, **kwargs):
        print('1, calling __new__')
        return super().__new__(cls)

    def __init__(self, x):
        print('2, calling __init__')
        self.x = x

a = A(1)
# 1, calling __new__
# 2, calling __init__

import dis
c = A.__new__.__code__
# dis.dis(c)
#   --           COPY_FREE_VARS           1

#    6           RESUME                   0

#    7           LOAD_GLOBAL              1 (print + NULL)
#                LOAD_CONST               0 ('1, calling __new__')
#                CALL                     1
#                POP_TOP

#    8           LOAD_GLOBAL              2 (super)
#                LOAD_DEREF               3 (__class__)
#                LOAD_FAST_BORROW         0 (cls)
#                LOAD_SUPER_ATTR          9 (__new__ + NULL|self)
#                LOAD_FAST_BORROW         0 (cls)
#                CALL                     1
#                RETURN_VALUE


class MyString(str):
    def __new__(cls, s):
        s = s.strip()
        return str.__new__(cls, s)

mys = MyString("  hello  ")
print(mys)
# hello

# why do this? - strings are immutable
# the string doesnt exist before __new__, but it does after 
# __new__ and before __init__
#
# if we try to reassign the attributes, since MyString inherits
# from the string class, the actual mys object will still point
# to the original string


class B:
    def __new__(cls):
        print('1, calling __new__')

    def __init__(self, x=1, y=2, z=3):
        print('2, calling __init__')
        self.x = x
        self.y = y
        self.z = z

b = B()
# 1, calling __new__
# __init__ isnt called here because b is None, no object was returned by __new__

class C:
    def __new__(cls):
        return "hello"

    def __init__(self):
        pass

c = C()
print(c, type(c))
# hello <class 'str'>
# this works -> new can return any object