#4.	Remove Duplicates: Remove duplicate characters from a string.

user_input = input("Enter your string: ")
seen = set()
input_list = []

for char in user_input:
    if char not in seen:
        seen.add(char)
        input_list.append(char)
new_input_list = ''.join(input_list)
print(new_input_list)
