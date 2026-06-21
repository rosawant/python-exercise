# Creating string
s = "Hello"
s = 'Hello'
s = """Hello World"""

# Accessing string characters
s = "Python"

print(s[0])    # P
print(s[-1])   # n

# String slicing
s = "Python"
print(s[0:3])   #or print(s[:3]) # Pyt --> Python by default starts from 0 index
print(s[2:])    # thon
print(s[:4])    # Pyth
print(s[::-1])  # nohtyP #reverse string
print(s[:])   # Python

# Python slicing
# syntax: string[start:stop:step]
# start → index to begin from (inclusive)
# stop → index to end at (exclusive)
# step → how many positions to move each time

print(s[::2])  # Pto # Omits 2 characters from the string
# this is euovalent to print(s[0:len(s):2]) 
# Take every 2nd character from the string starting from index 0 to the end of the string
print(s[1::2])  # yhn # Take every 2nd character from the string starting from index 1 to the end of the string
print(s[1:5:2])  # yh # Take every 2nd character from the string starting from index 1 to index 5 (exclusive)
# String concatenation
fname = "Roshan"
lname = "Sawant"

full = fname + " " + lname
print(full)

# String formatting
name = "Roshan"
age = 25
print(f"My name is {name} and I am {age} years old.") # My name is Roshan and I am 25 years old.#   
print("My name is {name} and I am {age} years old.") # My name is {name} and I am {age} years old.#   

print(f"{2+2}") # 4 # with f string we can use any expression inside the curly braces and it will be evaluated and the result will be included in the string
# String methods
s = "  Hello World  "
print(s.upper())      # HELLO WORLD
print(s.lower())      # hello world
print(s.strip())      # Hello World #remove spaces from the beginning and end of the string
print(s.replace("Hello", "Hi"))  # Hi World
print(s.split(" "))   # ['', '', 'Hello', 'World', '', ''] #split the string into a list of words using space as a delimiter

# String membership
s = "Python"
print("P" in s)      # True
print("Java" not in s)  # True  

# String immutability
s = "Python"
# s[0] = "J"  # This will raise an error because strings are immutable

# String length
s = "Python"
print(len(s))  # 6


# String methods continued
s = "Python Programming"
print(s.startswith("Python"))  # True
print(s.endswith("Programming"))  # True

# String methods continued
s = "Python Programming"
print(s.find("Programming"))  # 7   

# String methods continued
s = "Python Programming"
print(s.count("o"))  # 2
# String methods continued
s = "Python Programming"
print(s.isalpha())  # False # check if all characters in the string are alphabetic # there is space so this will return false
print(s.isalnum())  # False # check if all characters in the string are alphanumeric (letters and numbers only)
print(s.isdigit())  # False

# String methods continued
s = "Python"
print(s.isupper())  # False
print(s.islower())  # False
# Remove whitespace from the beginning and end of the string
s = "  Python  "

print(s.strip()) # Python
print(s.lstrip()) # Python # Remove whitespace from the left side of the string
print(s.rstrip()) # Python # Remove whitespace from the right side of the string
# Count the number of occurrences of a substring in the string
s = "banana"

print(s.count("a")) # 3
# Startswith and ends with
s = "file.txt"

print(s.startswith("file"))
print(s.endswith(".txt"))

# operator
print("My name is %s and age is %d" % (name, age))
# partition
email = "user@gmail.com"

print(email.partition("@")) # ('user', '@', 'gmail.com')
# String comparison
print("abc" == "abc")
print("abc" < "xyz")
# Remove duplicate characters from a string
s = "programming"

result = "".join(dict.fromkeys(s))
print(result)# progamin
# Check if a string is a palindrome # palindrome is a string that reads the same forwards and backwards
s = "madam"
if s == s[::-1]:
    print(f"{s} is a palindrome") #madam is a palindrome

# Split the string into a list of words
s = "a,b,cd"

print(s.split(",")) #['a', 'b', 'cd']
#join the list of words into a single string
words = ['a', 'b', 'c']

print("-".join(words)) #a-b-c
# String methods continued
s = "PYthon"
print(s.title())  # Python  

# String methods continued
s = "python"
print(s.capitalize())  # Python 
# String methods continued
s = "Python"
print(s.center(20, "*"))  # *******Python********
# String methods continued
s = "Python"
print(s.ljust(20, "*"))  # Python***************
# String methods continued
s = "Python"
print(s.rjust(20, "*"))  # ***************Python
# String methods continued
s = "Python"
print(s.zfill(10))  # 0000Python
# String methods continued
s = "Python"
print(s.swapcase())  # pYTHON
# String methods continued
s = "Python"
print(s.isidentifier())  # True
# String methods continued
s = "Python"
print(s.isprintable())  # True
# String methods continued
s = "Python"
print(s.isascii())  # True
# String methods continued
s = "Python"
print(s.partition("thon"))  # ('Py', 'thon', '')    
# String methods continued
s = "Python"
print(s.rpartition("thon"))  # ('Py', 'thon', '')
# String methods continued
s = "Python"
print(s.splitlines())  # ['Python']
# String methods continued
s = "Python"
print(s.expandtabs())  # Python
# String methods continued
s = "Python"
print(s.encode())  # b'Python'
# String methods continued
s = "Python"
print(s.format())  # Python
# String methods continued
s = "Python"
print(s.format_map({}))  # Python
#   String methods continued
s = "Python"
print(s.isnumeric())  # False
# String methods continued
s = "Python"
print(s.isdecimal())  # False
