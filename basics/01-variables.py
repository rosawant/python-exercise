str_var = "roshan"
float_var = 3.14
num_var = 42

longparagraph_string = """
This is a paragraph string. It can be used to demonstrate how to handle paragraph strings in Python. You can use triple quotes to create multi-line strings, which can be very useful for documentation or when you need to include line breaks in your string.
"""

print(len(str_var)) #ans: 6
#print(len(float_var))#TypeError: object of type 'float' has no len()
#print(len(num_var)) #TypeError: object of type 'int' has no len()

print(str_var.upper()) #ans: ROSHAN
print(str_var.lower()) #ans: roshan
print(str_var.capitalize()) #ans: Roshan
print(str_var.title()) #ans: Roshan
print(str_var.strip()) #ans: roshan
print(str_var.replace("roshan", "python")) #ans: python

print(str_var.split("o")) #ans: ['r', 'shan']