# Find Maximum and Minimum: Return the max and min from a list.

a = [4,3,5,252,52425,2323,2525,5]

# ist method
# print(max(a), min(a))

#second method
b = sorted(a)
print(b[0],b[-1])

#third method looping
min_value = a[0]
max_value = a[0]

for num in a:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print(min_value,max_value)


