# ellipsis are for a placeholder in the code - implement later
# an actual object -> with a type and a list of attributes
#
# as an internal type, ellipsis is anon, so we cant just say 
# ellipsis.__bases__
# Ellipsis, is an object instance of the class ellipsis, which
# is anonymous 

class A:
    ...  # this works


x = ...

print(type(x))
# <class 'ellipsis'

print(type(x).__bases__)
# (<class 'object'>,)
# returns a tuple of all direct parent classes
# cant do ellipsis.__bases__, explained above