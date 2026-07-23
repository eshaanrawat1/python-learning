# continuing on understanding garbage collection and an extension 
# of the code in finalizer.py
#
# python uses reference counts to determine garbage collection

import sys
import weakref

class A:
    def __del__(self):
        print('deleting...')

a = A()

print(sys.getrefcount(a))
# 2
# deleting...
#
# why is it 2? 
# when we call a function, we copy the pointer to a by value
# so 2 pointers exist (original object and function param pointer)

ref = weakref.ref(a)
print(sys.getrefcount(a))
# 2
#
# still 2, a weak reference doesn't count as a new reference to an object
# if the ref count is 0, even if there are weak references remaining, an
# object is free to get garbage collected 

print(ref)
print(ref())
# <weakref at 0x100953290; to 'A' at 0x100a4cd70>
# <__main__.A object at 0x100a4cd70>

# we can also use weakref.proxy so we don't have to call ref()
ref2 = weakref.proxy(a)
print(ref2)
# <__main__.A object at 0x109e24d70>

# weakref.finalize is considered a more robust way of handling
# specific actions right before an object is being garbage collected