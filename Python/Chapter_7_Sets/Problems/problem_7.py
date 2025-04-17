#Take a string input and store all unique characters in a set. Count how many vowels are present


user_input = input("Enter your string: ")
char_set = set()
vowels = ['a','e','i','o','u']
vowel_set = set()

for char in user_input:
    
    char_set.add(char)
    for vow in char_set:
        if vow in vowels:
            vowel_set.add(vow)

length = len(vowel_set)
print(length, end=" ")
print(char_set)