#10.	Custom Sorting: Sort a list of strings based on their lengths

a = ['apple', 'banana', 'kiwi', 'grape']

for i in range(len(a)-1):

    for j in range(len(a)-1-i):
        if len(a[j]) > len(a[j+1]):
            a[j],a[j+1] = a[j+1], a[j]

print(a)