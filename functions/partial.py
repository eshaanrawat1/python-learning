# functools partial gives a way to to freeze certain arguments of a function
#
# partials also are pickleable - while lambdas are not, allows us to use with
# multiprocessing

from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)

print(square(5))
# 25
# what we expect, base=5, exp is already frozen as 2

square2 = partial(power, 2)
print(square2(5))
# 32
# partial fills values from left to right
# it assigns base=2 if not specified as a keyword arg,
# so the value returned is 2^5

# print(square2(7, 3))
# Traceback (most recent call last):
#   File "functions/partial.py", line 21, in <module>
#     print(square2(7, 3))
#           ~~~~~~~^^^^^^
# TypeError: power() takes 2 positional arguments but 3 were given
#
# we cannot overwrite a positional argument
# square2 already has base set to 2

print(square(7, exp=3))
# 343
# explicitly overriding a keyword argument works


# partials also solve the late binding problem which lambdas have
handlers = [lambda: print(i) for i in range(3)]
for h in handlers:
    h() 

# 2
# 2
# 2   
# wrong, lambda is late binding - it waits until the loop is done,
# then all lambda functions bind i=2

handlers = [partial(print, i) for i in range(3)]
for h in handlers:
    h() 

# 0
# 1
# 2
# correct, partial binds immediately