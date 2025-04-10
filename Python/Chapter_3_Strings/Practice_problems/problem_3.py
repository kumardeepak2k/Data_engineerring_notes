#3.	Check Palindrome: Check if a string reads the same forward and backward.

user_input = input("Enter your string: ")
reversed_input = ''

for char in user_input:
    reversed_input = char + reversed_input

if reversed_input == user_input:
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")