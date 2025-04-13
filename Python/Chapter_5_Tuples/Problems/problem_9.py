#9.	Tuple Sorting: Sort a list of tuples by second element, e.g., [(1, 3), (2, 2)].

a = [(1, 3), (2, 2), (4, 5), (0, 1)] 

#using sort
sorted_a = sorted(a, key= lambda x:x[1], reverse=False)
print(sorted_a)

#without using sort 
length = len(a)

for i in range(length):
    keep_runnning = False
    for j in range(0, length - 1 - i):
        if a[j][1] > a[j+1][1]:
            a[j], a[j+1] = a[j+1], a[j]
            keep_runnning = True
    if not keep_runnning:
        break
print(a)
