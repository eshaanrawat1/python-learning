# basic error handling

try:
    x = 5
    raise ValueError("aaa")
except ValueError as e:
    print('ValueError happened:', e)
finally:
    print("finally")

# ValueError happened: aaa
# finally
#
# we can raise an error with a message - which gets printed by the error
# finally always runs after the try except block
#
# we can use except Exception as e to get the actual error as an 
# object -> e (or whatever name we choose)


try:
    x = 5
except ValueError:
    print("error")
else:
    print("no error happened")
finally:
    print("finally ran")

# no error happened
# finally ran
#
# else runs only when the try block runs normally 