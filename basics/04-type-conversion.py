x = input("x: ") # input() function takes input from the user and returns it as a string
print(type(x)) # <class 'str'> # the type of x is string
y = x +1 # TypeError: can only concatenate str (not "int") to str # we cannot add an integer to a string
# we need to convert the string to an integer before we can add 1 to it
y = int(x) + 1 # we can use the int() function to convert the string to an integer
print(type(y)) # <class 'int'> # the type of y is integer


# Type conversion
a = "10"
int(a) # convert string to integer
float(a) # 10.0 convert string to float
str(a) # convert string to string (no change)
# Boolean Type conversion
# falsy values: '', 0, 0.0, [], {}, set(), None
# truthy values: any non-empty string, any non-zero number, any non-empty list, any non-empty dictionary, any non-empty set, True
bool("") # False
bool(1) # True