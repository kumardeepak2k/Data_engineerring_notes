#Remove Duplicates: Remove duplicates without using set()

a = [2, 4, 100, 45, 99, 100, 87]

new_a = []

for num in a:
    if num not in new_a:
        new_a.append(num)
    else:
        continue

print(new_a)

