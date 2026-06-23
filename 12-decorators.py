# # decorators: A Python decorator is a design pattern that allows you to modify or extend the behavior of a function 
# # or class without altering its actual source code

# # function decorators:
# # @mydecorator
# # def docomething():
# #     pass

# def start_end_decorator(func):
#     def wrapper():
#         print("Start..")
#         func()
#         print("End..")
#     return wrapper

# @start_end_decorator
# def print_name():
#     print("Alex")

# # Start..
# # Alex
# # End..  

## example 2
# using *args--> argument , **kwargs--> keyword argument : with this we can pass n number of arguments
import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start..")
        result = func(*args, **kwargs)
        print("End..")
        return result
    return wrapper

@start_end_decorator
def add_num(x):
    result = x + 5
    print(result)
    return result

result = add_num(2)


# ####final decorator template
# # with wraps the identity of the main fucntions will be maitained
# from functools import wraps
# def my_decorator(func):
#     wraps(func)
#     def wrapper(*args, **kwargs):
#         #Do something ..
#         result = func(*args, **kwargs)
#         return result
#     return wrapper

# ## example 2
# from functools import wraps

# def repeat(num_times):
#     def my_decorator(func):
#         wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return my_decorator
# @repeat(num_times=4)
# def greet(name):
#     print(f"Hello {name}")

# greet("Alex")

