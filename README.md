(e.g., reversing words in a string, palindrome, string manipulation) in a shared online compiler. 
# 1. Find the largest number in list
```
option:1 
numbers = [10, 24, 76, 23, 12]
largest = max(numbers)

print(largest)  # Output: 76

option2:
numbers = [10, 24, 76, 23, 12]

# Assume the first element is the largest
largest = numbers[0]

# Compare every number with the current largest value
for num in numbers:
    if num > largest:
        largest = num

print(largest)  # Output: 76

# option3:
numbers = [10, 24, 76, 23, 12]

# Sort the list in place
numbers.sort()

# Access the last item using negative indexing
largest = numbers[-1]

print(largest)  # Output: 76
```
# 2. Reverse String
```
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))  # Output: nohtyP

```
# 3. Check palindrome
```
option1: 
name = "naman"
if name == name[::-1]:
    print(f"{name}" is palindrome)

option2:

def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))  # Output: True
```
# 4. Find second larget number 
```
def second_largest(numbers):
    unique_nums = list(set(numbers))
    unique_nums.sort(reverse=True)
    return unique_nums[1] if len(unique_nums) >= 2 else None

print(second_largest([10, 5, 20, 20, 8]))  # Output: 10
```
# 5. Check if number is Prime
```
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(17))  # True
print(is_prime(18))  # False
```
# 6. Swap two string
```
a = "Hello"
b = "World"

a, b = b, a

print(a)  # World
print(b)  # Hello
```
# 7. Swap first and last character
```
def swap_string(s):
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]

print(swap_string("python"))
```
# 8. Count Vowels in a String
```
def count_vowels(s):
    # Define vowels
    vowels = "aeiouAEIOU"
    # Initialize count
    count = 0
    # Count vowels
    for char in s:
        if char in vowels:
            count += 1
    return count

count_vowels("hello") #2
```
# 9. Check if number is even from the list
```
a = [1, 2, 3, 4, 5, 6]
even_num = filter(lambda x: x%2 == 0, a)
print(list(even_num)) #[2, 4, 6]
```