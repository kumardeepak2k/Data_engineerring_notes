
# 7.	Swap Case: Convert uppercase letters to lowercase and vice versa.

sentence = "Hello World!"

# Initialize an empty string for the result
swapped_sentence = ""

# Loop through each character in the sentence
for char in sentence:
    if char.islower():
        swapped_sentence += char.upper()  # Convert lowercase to uppercase
    elif char.isupper():
        swapped_sentence += char.lower()  # Convert uppercase to lowercase
    else:
        swapped_sentence += char  # Non-alphabetic characters remain the same

# Print the swapped sentence
print(swapped_sentence)
