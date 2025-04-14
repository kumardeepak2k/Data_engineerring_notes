# Frequency Counter: Count frequency of characters in a string using dictionary.

name = "Deepak kUmar34241"

counter = {}

# for char in name.lower():
#     if char != ' ':
#         if char in counter:
#             counter[char]+=1
#         else:
#             counter.update({char:1})

print(counter)

#CLEANER LOGIC
for char in name:
    counter[char] = counter.get(char, 0) + 1
print(counter)
