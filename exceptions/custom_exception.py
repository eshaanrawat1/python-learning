# we can create custom exceptions that inherit from the Exception class
# the except block catches all subclasses of a given error, so bare 
# excepts can be dangerous 

print(ValueError.__mro__)
# (<class 'ValueError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
# 
# most errors inherit from Exception
# all errors inherit from BaseException

print(SystemExit.__mro__)
print(KeyboardInterrupt.__mro__)
print(GeneratorExit.__mro__)

# (<class 'SystemExit'>, <class 'BaseException'>, <class 'object'>)
# (<class 'KeyboardInterrupt'>, <class 'BaseException'>, <class 'object'>)
# (<class 'GeneratorExit'>, <class 'BaseException'>, <class 'object'>)
#
# these 3 exceptions are special - they inherit directly 
# from BaseException, not from Exception. this is because we want
# to catch these errors explicitly

try:
    print(1/0)
except:
    print("catch all!")

# catch all!


class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(f"{message}")
        self.message = message


try:
    x = 5
    raise MyCustomError("some test message")
except Exception as e:
    print("error happened:", e)

# error happened: some test message

try:
    for i in range(10**9):
        pass
except KeyboardInterrupt as e:
    print("interrupted the long loop", e)

# ^Cinterrupted the long loop