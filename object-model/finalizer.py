# __del__ serves as a finalizer that is called right before an 
# object is being garbage collected. in cpython, this is when the 
# reference count of an object reaches 0
#
# cpython -> runs immediately when refcount hits 0
# pypy -> runs eventually after refcount hits 0 
# so del is unreliable timing wise to rely on immediate destruction guarantees

class A:
    def __new__(cls):
        print("1. __new__")
        return object.__new__(cls)

    def __init__(self):
        print("2. __init__")

    def __del__(self):
        print("3. __del__")

# a = A()
# del a
# 1. __new__
# 2. __init__
# 3. __del__

# a1 = A()
# a2 = a3 = a1 

# print('deleting a1')
# del a1
# print('deleting a2')
# del a2
# print('deleting a3')
# del a3
# 1. __new__
# 2. __init__
# deleting a1
# deleting a2
# deleting a3
# 3. __del__ (deleted after all references were deleted)

# a1 = A()
# a2 = a3 = a1

# print('reassign a1')
# a1 = 4
# print('reassign a2')
# a2 = 4
# print('reassign a3')
# a3 = 4
# 1. __new__
# 2. __init__
# reassign a1
# reassign a2
# reassign a3
# 3. __del__ (called when no references to original object exist)

class B:
    def __del__(self):
        print("deleting!")

b1 = B()
b2 = B()
b1.other = b2
b2.other = b1

print('deleting b1...')
del b1
print('deleting b2...')
del b2
print('breakpoint...')
# b1 and b2 arent immediately deleted due to circular references
