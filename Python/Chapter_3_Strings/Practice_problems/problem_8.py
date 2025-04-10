#8.	Anagram Checker: Check if two strings are anagrams (e.g., “listen” and “silent”).

from collections import Counter

input_1 = input("Enter your first word: ").strip().lower()
input_2 = input("Enter your second word: ").strip().lower()

if len(input_1) != len(input_2):
    print("Not an anagram")
else:
    frequency_1 = Counter(input_1)
    frequency_2 = Counter(input_2)
    if frequency_1 == frequency_2:
        print("Anagram")
    else:
        print("Not an anagram")
print (frequency_1)