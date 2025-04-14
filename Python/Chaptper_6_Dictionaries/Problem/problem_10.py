#10.	Dictionary from List: Create a dictionary from a list of tuples like [("a", 1), ("b", 2)].

list = [("a",1), ("b",2),("c",3)]
dict = {}

for tup in list:
    dict[tup[0]] = tup[1]
print(dict)

#concise
list = [("a", 1), ("b", 2), ("c", 3)]
dict = dict(list)

print(dict)
