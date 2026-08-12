# the cause dunder is the second main dunder when dealing with exceptions 
# using the from keyword, we can say this error is caused by that error
# 
# cause is never set automatically, only with the from keyword
# doing so also sets suppress context to True

def f():
    raise ValueError("aaa") from ZeroDivisionError("something happened")
# f()
#
# this result below shows a human readable format with "direct cause of"

# ZeroDivisionError: something happened

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "exceptions/cause_dunder.py", line 9, in <module>
#     f()
#     ~^^
#   File "exceptions/cause_dunder.py", line 8, in f
#     raise ValueError("aaa") from ZeroDivisionError("something happened")
# ValueError: aaa

def f2():
    try:
        raise ValueError("aaa") from ZeroDivisionError("something happened")
    except ValueError as e:
        print(e.__cause__)
        print(e.__suppress_context__)

f2()
# something happened
# True

def f3():
    try:
        raise ValueError("aaa") from None
    except ValueError as e:
        print(e.__cause__)
        print(e.__suppress_context__)
f3()
# None
# True
#
# raise from None is valid and limits the traceback to just this error
# it also sets suppress context to True