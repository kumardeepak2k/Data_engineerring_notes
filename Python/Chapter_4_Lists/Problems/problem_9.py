#9.	List Compression: Compress a list by removing consecutive duplicates.

a = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

new_list = []

for i in range(len(a)):
    if i == 0 or a[i] != a[i-1]:
        new_list.append(a[i])
print(new_list)
