# 01 - Palindrome check
s = "madam"

print(s == s[::-1])

# 02 - Reverse a string
str = "roshan"
# option1
print(str[::-1])
# option2
print(''.join(reversed(str)))

# 03 - Swap two strings
str1 = "hello"
str2 = "world"
str1, str2 = str2, str1
print(str1, str2)

# 04 - Count Vowels and Consonants in a String
s = "Python Programming"

count = sum(1 for c in s.lower() if c in "aeiou")

print(count)
#option2
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count
s = "madam"
if s == s[::-1]:
    print(f"{s} is a palindrome")

vowels, consonants = count_vowels_consonants(s)
print(f"Vowels: {vowels}, Consonants: {consonants}")

# 05- Frequency of characters in a string
from collections import Counter

s = "banana"

print(Counter(s))

# 06 - Remove duplicate characters from a string
s = "programming"
print(''.join(dict.fromkeys(s))) #progamin

# 07 - first non-repeating character in a string
s = "aabbcdde"

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
 # 08 - Remove special characters from a string
import re

s = "Hello@123#"

print(re.sub(r'[^a-zA-Z0-9]', '', s)) #Hello123