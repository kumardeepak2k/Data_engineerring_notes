#5.	Merge Dictionaries: Merge two dictionaries into one.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

#update
# dict1.update(dict2)
# print(dict1)

# new_dict = {**dict1, **dict2}
# print(new_dict)

#using | operator
new_dict = dict1 | dict2
print (new_dict)

# using counter
from collections import Counter

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

merged = dict(Counter(d1) + Counter(d2))
print(merged)
