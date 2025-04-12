#Rotate List: Rotate the list to the right by k steps.
 
#rotate right
a = [1, 2, 3, 4, 5]
k = 2

# for _ in range(k):
#     last_element = a.pop()
#     a.insert(0,last_element)

# print(a)

#rotate left

for _ in range(k):
    first_element = a.pop(0)
    a.append(first_element)
print(a)