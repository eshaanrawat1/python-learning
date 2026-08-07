# any class that implements one of __get__, __set__, or __delete__ 
# automatically becomes a descriptor -> allows custom behavior
# on attribute access, assignment, or deletion


class CustomDescriptor:
    def __get__(self, instance, owner=None):
        print(f'self={self}, instance={instance}, owner={owner}')
        return 42

class A:
    x = CustomDescriptor()

    def __init__(self, a, b):
        self.a = a 
        self.b = b 

a = A(4,5)
print(a.a, a.b, a.x)
# self=<__main__.CustomDescriptor object at 0x109516120>, 
# instance=<__main__.A object at 0x109515e80>, owner=<class '__main__.A'>
# 4 5 42
#
# a doesn't have an x attribute, but x is a class atribute

print(A.__dict__['x'])
# <__main__.CustomDescriptor object at 0x10098a120>

# two types of descriptors
# data descriptors implement __get__ and (__set__ or __delete__)
# non data descriptors implement __get__ only 
# this affects precedence in attr lookup


class DataDesc:
    def __get__(self, instance, owner=None):
        return 100

    def __set__(self, instance, value):
        instance.__dict__['x'] = 101


class NonDataDesc:
    def __get__(self, instance, owner=None):
        return 200


class B:
    x = DataDesc()
    y = NonDataDesc()

b = B()
print(b.x)
# 100

print(b.y)
# 200

b.x = 50
print(b.x, b.__dict__)
# 100 {'x': 101}
# x is a data descriptor, (higher precedence than object dict)
# even though x=101 in the object dict, the __get__ method is called first

b.y = 250
print(b.y, b.__dict__)
# 250 {'x': 101, 'y': 250}
# y is a non data descriptor, which has lower precedence than 
# an object dict

b.__dict__['y'] = 300
print(b.y, b.__dict__)
# 300 {'x': 101, 'y': 300}
