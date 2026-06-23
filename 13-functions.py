# def foo(a, b, c):
#     print(a, b, c)

# # positional arg:
# foo(1, 2, 3)
# foo(a=1, b=2, c=3)
# foo(1, b=2, c=3) # but you can write a positional arg afteer kwyword arg like foo(1, b=2, 3)

# # defautl arg
# # Default arguments must be at the end
# # After args you cant pass argument , you have to pass kwars
# # Not Allowed: foo(*args, a, 2)
# # Allowed: foo(*args, a=1, b=2) 
# # *args -> 
#       passed directly to fun lik foo(1,2,3)        
#       this al list (for i in args)

# #  **kwargs --> 
#       passed with the keyword like foo(one=1, two=2, name="alex")
#       this is a dict (for key in kwargs: print(key, kwargs[key])) 
# def foo(a, b, c, d=4): # can set default value for d
#     print(a, b, c, d)
# foo(1, 2, 3, 5) # can overwrite default value


# example 1
def foo(a, b, *args, **kwargs):
    for i in args:
        print(i)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, six=6, seven=7) 

# example 2
# note: length and keys of arguments must match function apramater

def foo(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2, "c": 3}
foo(*my_list) # *args
foo(**my_dict) # **kwargs

## Global vs local variable
def print_num():
    global number
    number = 3

number = 1
print_num() # 3
