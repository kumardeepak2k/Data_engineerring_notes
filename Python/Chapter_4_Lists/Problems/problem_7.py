#Pair Sum: Find all pairs in a list that sum to a target value.

a = [2, 4, 3, 5, 7, 6]  # List of numbers
target = 10
# pair = []

# #bruteforce
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+ a[j] == target:
#             pair.append((a[i],a[j]))

# print(pair)

#optimised way
seen = set()
pair = []

for num in a:
    complement = target - num
    if complement in seen: 
        pair.append((num,complement)) 
    else:
        seen.add(num)
print(pair)
