### For loop

## Example 1
for number in range(3):
    print("Ateempt", number)
#Attempt 0
#Attempt 1
#Attempt 2
## Example 2
# To make it better we can use number + 1
for number in range(3):
    print("Ateempt", number + 1)
# Ateempt 1
# Ateempt 2
# Ateempt 3
## Example 3
for number in range(3):
    print("Attempt", number + 1 , (number + 1) * ".")
# output:
# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...
## Example 4
for number in range(1,4):
    print("Attempt", number , number * ".")
#output:
# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...
## Example 5
for number in range(1,10,2): # step by 2
    print("Attempt", number , number * ".")
# Attempt 1 .
# Attempt 3 ...
# Attempt 5 .....
# Attempt 7 .......
# Attempt 9 .........

## Example 6
success = False

for num in range(1,4):
    print("Attempt", num)
    if success: # check if success is true
        print("Atempt success")
        break # Exited from loop
else:
    print("Atempted 3 times but failed")
# Attempt 1
# Attempt 2
# Attempt 3
# Atempted 3 times but failed

### Nested Loops

## Example 1
for x in range(5):
    for y in range(3):
        print(f"{x}, {y}")

## Iterable objects in Python
# range()
# string
# list --> [1,2,3,4]
# 