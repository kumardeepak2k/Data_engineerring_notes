#A = [1,2,3,4], B = [3,4,5,6], C = [5,6,7,8]
# Write a program to find:

# Elements common to all three

# Elements only in one list

A = [1,2,3,4]
B = [3,4,5,6]
C = [4,5,6,7,8]

a,b,c = set(A),set(B),set(C)

inter = a.intersection(b,c)
print(inter)

only_in_a = a - (b | c)
only_in_b = b - (a | c)
only_in_c = c - (a | b)

only_in_one = only_in_a | only_in_b | only_in_c
print("Elements only in one list:", only_in_one)
