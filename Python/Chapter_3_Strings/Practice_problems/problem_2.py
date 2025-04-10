#Reverse a String: Reverse a given string using slicing.

user_input = input("Enter your string: ")
reversed_input = user_input[::-1]
print(reversed_input)

#without slicing

user_input = input("Enter your string: ")
reversed_input = ''

for char in user_input:
    reversed_input = char + reversed_input
print(reversed_input)