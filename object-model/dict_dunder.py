# python supports the model that everything is an object (this is pythonic)
# which means every object has a dict with its attributes

class C: ...
def foo(): ...
def bar(): ...

print(C.__dict__)  # print(vars(C)) -> same thing as dict dunder

# {'__module__': '__main__', '__firstlineno__': 4, '__static_attributes__': (), 
# '__dict__': <attribute '__dict__' of 'C' objects>, '__weakref__': <attribute '__weakref__' of 'C' objects>, '__doc__': None}

print(type(C.__dict__))
# <class 'mappingproxy'>
# mappingproxy is a read only view of __dict__

print(foo.__dict__)
# {}

bar.retries = 3
bar.dummy_attr = "hello"
print(bar.__dict__)
# {'retries': 3, 'dummy_attr': 'hello'}
# retries (and other function attributes) can be a useful pattern for decorators 

c = C()
c.__dict__['x'] = 15
print(c.x)
# 15


class D:
    @property
    def x(self):
        return 21

    def m(self):
        return "class"

d = D()
print(D.__dict__['x'])
# <property object at 0x107800bd0>

d.__dict__['x'] = 15
print(d.x, d.__dict__)
# 21 {'x': 15}
# prints 21 because of object lookup order -> d.x calls getattribute which first looks
# to data descriptors, then looks to the object dict
# 
# @property makes x a data descriptor attribute - which means we care about the class
# level of what this is (defines get and set methods), so an overwrite in the instance
# dict is ignored

d.__dict__["m"] = lambda : "instance"
print(d.m())
# instance
# m is not a data descriptor, the overwrite in dict wins