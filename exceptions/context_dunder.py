# the context dunder is one of two main dunders when dealing with exceptions
# __context__ tells an error what happened during the handling of this error
#
# __context__ is filled in automatically by python

try:
    1 / 0
except ZeroDivisionError as outer:
    try:
        raise ValueError("aaaaa")
    except ValueError as inner:
        print("outer            :", repr(outer))
        print("outer.__context__:", repr(outer.__context__))
        print("inner            :", repr(inner))
        print("inner.__context__:", repr(inner.__context__))
        print("same object?     :", inner.__context__ is outer)

# outer            : ZeroDivisionError('division by zero')
# outer.__context__: None
# inner            : ValueError('aaaaa')
# inner.__context__: ZeroDivisionError('division by zero')
# same object?     : True
#
# if exception B happens while exception A is being handled, then 
# B.__context__ = A