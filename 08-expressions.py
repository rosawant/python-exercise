# # Errors and exceptions
# x = -5
# if x <= 5:
#     raise Exception(f"{x} should be positive")
# # Exception: -5 should be positive

# #or
# x = -5
# assert(x>=0), 'x is not positive'
# # AssertionError: x is not positive

# # try and except
# try:
#     a = 5 / 0 #ZeroDivision error
# except Exception as e:
#     print(e)

# # example 2
# try:
#     a = 5 / 1
#     b = 1 + 'hello'
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("no exceptions, all good")
# finally: # this block will run always ..mostly used for cleanup tasks
#     print("cleaning up..")

## Create custom exception

class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        
def test_val(x):
    if x > 100:
        raise ValueTooHighError(f"{x} is higher than 100")
    if x < 5:
        raise ValueTooSmallError("Value is too small", x)
# test_val(150) #__main__.ValueTooHighError: 150 is higher than 100

try:
    test_val(1)
except ValueTooHighError as e:
    print(e) #200 is higher than 100
except ValueTooSmallError as e:
    print(e.message, e.value)