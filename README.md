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

option3:
def is_palindrome(s: str) -> bool:
    clean_str = "".join(char.lower() for char in s if char.isalnum())
    return clean_str == clean_str[::-1]

print(is_palindrome("A man, a plan, a canal: Panama")) # Output: True
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
# 10. Common Characters Between Two Strings
## with set
```
s1 = "hello"
s2 = "world"

common = set(s1) & set(s2)

print("Common characters:", common)
```
## without set
```
s1 = "hello"
s2 = "world"

print("Common characters:")
for ch in s1:
    if ch in s2:
        print(ch, end=" ")
```
# 11.Characters Present in First String but Not in Second
```
s1 = "hello"
s2 = "world"

not_common = set(s1) - set(s2)

print("Not common in s1:", not_common)
```
```

```
# 12. Characters Not Common in Either String (Symmetric Difference)
```
s1 = "hello"
s2 = "world"

not_common = set(s1) ^ set(s2)

print("Not common characters:", not_common)
```
# 13 Count character freqenecies
```
from collections import Counter

def char_frequency(s: str) -> dict:
    # Efficient O(n) lookup using built-in Counter
    return dict(Counter(s))

print(char_frequency("apple")) # Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
```
# 14  Remove Duplicates from a List
```
# Method 1: Fast but does not preserve original element order
def remove_duplicates_fast(lst: list) -> list:
    return list(set(lst))

# Method 2: Preserves insertion order (Python 3.7+)
def remove_duplicates_ordered(lst: list) -> list:
    return list(dict.fromkeys(lst))

nums = [1, 2, 2, 3, 4, 4, 1]
print(remove_duplicates_ordered(nums)) # Output: [1, 2, 3, 4]
```