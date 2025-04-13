#	Count Element: Count how many times a given value appears in a tuple.


repeated_tuple = (5, 10, 5, 20, 5)

a = 10

count = 0

for num in repeated_tuple:
    if a == num:
        count += 1

print(count)

