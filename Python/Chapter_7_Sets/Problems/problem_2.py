# #Set Operations
# Given two sets, perform union, intersection, 
# and difference operations without using built-in methods like .union() or .intersection().

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersect_set = set()

union_set = set()


#union
for char in set1:
    union_set.add(char)
for char in set2:
    union_set.add(char)
print(union_set)

#intersection
for char in set1:
    if char in set2:
        intersect_set.add(char)

print(intersect_set)