# attribute lookup has a specific process where python knows where to 
# look next if an attribute isnt found at a specific location 
#
# every attribute lookup starts with __getattribute__
# __getattr__ is only called as a fallback when the normal lookup fails

class A:
    def __init__(self, x):
        self.x = x 

    def __getattr__(self, name):
        print('__getattr__ called', name)
        return 10

a = A(5)
print(a.x)
# 5
# what you'd expect, a.x lives in the object dict


print(a.y)
# __getattr__ called y
# 10
#
# normal attribute lookup fails, but __getattr__ is defined, returns 10


class B:
    def __init__(self, x):
        self.x = x 

    def __getattr__(self, name):
        print('__getattr__ called', name)
        return 10

    def __getattribute__(self, name):
        print('__getattribute__ called', name)
        return 15

    def foo(self):
        return "foo!"

b = B(2)
print(b.y)
# __getattribute__ called y
# 15

print(b.x)
# __getattribute__ called x
# 15
#
# __getattribute__ always runs no matter what. we set b.x = 2, but 
# the value returned is 15 
#
# since it runs always - any calls to self.<attr> will cause an infinite
# loop is self. is called insite __getattribute__ 

# print(b.foo())
#   File "object-model/attribute_lookup.py", line 59, in <module>
#     print(b.foo())
#           ~~~~~^^
# TypeError: 'int' object is not callable
# b.foo resolves to 15, cant call a method on an int

class C:
    x = 11
    def __getattribute__(self, name):
        print(f'C getattribute called: {name}')
        return super().__getattribute__(name)

class D:
    x = 12

class E(C, D):
    def __getattribute__(self, name):
        print(f'E getattribute called: {name}')
        return super().__getattribute__(name)

e = E()
print(e.x)
# E getattribute called: x
# C getattribute called: x
# 11
#
# since C is the first class with x in E's MRO
#
# 1. E's __getattribute__ is called
# 2. super goes to C's __getattribute__
# 3. super goes to object's __getattribute__
# 4. which goes to normal attribute lookup via MRO
# 5. C is the first class which implements x 


class F:
    def __getattr__(self, name):
        print('F getattr called')
        return 100

class G(F):
    pass

g = G()
print(g.x)
# F getattr called
# 100
#
# __getattr__ is inherited, so if a normal attribute lookup causes
# an attribute error, python looks for __getattr__ in the class's mro


class H:
    def __getattribute__(self, name):
        print('H getattribute called')
        return 111

class I(H):
    pass

i = I()
print(i.x)
# H getattribute called
# 111