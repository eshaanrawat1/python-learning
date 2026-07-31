# slots provide a way to forego the dict object in favor of 
# predictable behavior (and slightly optimized memory use)
# memory optimized due to array instead of hash table 
# (with some caveats since dicts are optimized in cpython)

class A:
    __slots__ = ('a', 'b')

    def __init__(self, a, b):
        self.a = a 
        self.b = b 

a = A(5, 6)
print(a.a, a.b)
# 5 6
# expected behavior

# a.c = 7
# AttributeError: 'A' object has no attribute 'c' and 
# no __dict__ for setting new attributes
#
# objects of class A have no __dict__, so we cannot assign variables
# an important distinction - the class still has a dict

print(A.__dict__)
# {'__module__': '__main__', '__firstlineno__': 4, '__slots__': ('a', 'b'), 
# '__init__': <function A.__init__ at 0x1057578a0>, 
# '__static_attributes__': ('a', 'b'), 'a': <member 'a' of 'A' objects>, 
# 'b': <member 'b' of 'A' objects>, '__doc__': None}


# inheritance with slots is an interesting case ->
# all classes in the inheritance chain must have slots, if even one does
# not, then python will give the objects a dict

class B:
    pass 

class C(B):
    __slots__ = ('x',)

    def __init__(self, x):
        self.x = x 

c = C(10)
c.y = 11
print(c.x, c.y)
# 10 11
# allowed because B has no slots 

print(c.__dict__)
# {'y': 11}
# but x is not in the dict

c.__dict__['x'] = 25
print(c.x, c.__dict__)
# 10 {'y': 11, 'x': 25}
# still 10 because slots makes each attr a data descriptor
# with __get__, __set__, and __delete__ methods