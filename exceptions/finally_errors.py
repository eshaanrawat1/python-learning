# finally runs at the end of a try-except-finally block but it has some
# behavior that can cause unusual errors. finally is basically a matter
# of saving state, so changes in finally can overwrite returns in a try block
#
# finally doesn't run in some cases, though
# 1. os.exit() -> bypasses it
# 2. killed process (segfault, shutdown, etc)
# 3. generator or infinite loop 

def f1():
    try:
        return "hello"
    finally:
        return "nope, overwritten"
    
print(f1())
# nope, overwritten

# exceptions/finally_errors.py:9: SyntaxWarning: 'return' in a 'finally' block
#   return "nope, overwritten"
#
# the return for try is saved, but overwritten when finally runs
# python gives us a syntax warning because of how returns in a finally
# block can be dangerous

# some more examples

def f2():
    try:
        raise ValueError
    finally:
        return "error swallowed"
    
print(f2())
# error swallowed


def f3():
    for _ in range(3):
        try:
            raise ValueError
        finally:
            continue
    print("done!")

f3()
# done!

def f4():
    try:
        raise ValueError("real problem")
    finally:
        raise RuntimeError("cleanup failed")

# f4()
# Traceback (most recent call last):
#   File "exceptions/finally_errors.py", line 46, in f4
#     raise ValueError("real problem")
# ValueError: real problem

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "exceptions/finally_errors.py", line 50, in <module>
#     f4()
#     ~~^^
#   File "exceptions/finally_errors.py", line 48, in f4
#     raise RuntimeError("cleanup failed")
# RuntimeError: cleanup failed
#
# the error is swallowed, but the context dunder fires, so we still 
# have the history of the ValueError being handled first


def f5():
    x = [1]
    try:
        return x
    finally:
        x.append(2)

print(f5())
# [1, 2]
# finally can still mutate state


def f6():
    x = 1
    try:
        return x
    finally:
        x = 2

print(f6())
# 1
# x isn't overwritten here because the return value is already bound
# only mutable objects are changed like above