temperature = 30
if temperature > 25:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's a lovely day")

# Ternary operator
temperature = 30
message = "It's a hot day" if temperature > 25 else "It's not a hot day"
print(message) # It's a hot day

#Logic operators : and, or, not
# example 1
temperature = 30
if temperature > 25 and temperature < 35:
    print("It's a hot day")

# example 2
## High income and good credit is already boolean values, so we can use them directly in the if statement and we don't need to compare them to True or False
high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# Example 3 with not operator
# if not student means if student is False, then the condition will be True and the code inside the if block will be executed
student = False
if not student:
    print("You are not a student")
else:
    print("You are a student")

# Example 4

high_income = True
good_credit = True
student = False

if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("not eligible")

# Chaining comparision operator
age = 22
if 18 <= age < 65:
    print("Eligible")

