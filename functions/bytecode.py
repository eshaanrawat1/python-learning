# tldr
#
# dis is used to disassemble code into python bytecode 
# can access the compiled code object of a func with __code__
#
# __code__ is only for functions, methods, generators
# not classes? -> because __code__ is for executable code


import dis

x = 3
def add_nums(y):
    s = x + y
    return s 

c = add_nums.__code__

print(c.co_argcount, c.co_varnames)
# 1 ('y', 's')

dis.dis(c) 
#   4           RESUME                   0

#   5           LOAD_GLOBAL              0 (x)
#               LOAD_FAST_BORROW         0 (y)
#               BINARY_OP                0 (+)
#               STORE_FAST               1 (s)

#   6           LOAD_FAST_BORROW         1 (s)
#               RETURN_VALUE



class A:
    pass

try:
    print(A.__code__)
except Exception as e:
    print('an error happened', e)
# an error happened type object 'A' has no attribute '__code__'