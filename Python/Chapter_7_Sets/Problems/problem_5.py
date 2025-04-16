#Symmetric Difference
# Implement symmetric difference between two sets manually, without using .symmetric_difference().

set1 = (1, 2, 3, 4)
set2 = (3, 4, 5, 6)
sd_a = set()

for char in set1:
    if char not in set2:
        sd_a.add(char)
print(sd_a)