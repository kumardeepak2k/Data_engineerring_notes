#Write a program to find common elements between two lists using sets.

set1 = [1, 2, 3, 4]
set2 = [3, 4, 5, 6]

set_11 = set(set1)
set_22 =  set(set2)

common_elements =  set_11.intersection(set_22)
union_elements = set_11.union(set_22)

print(common_elements)
print(union_elements)