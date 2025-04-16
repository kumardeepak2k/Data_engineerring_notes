
# Python Sets

## Introduction
- A **set** is an unordered collection of unique elements.
- Sets are mutable (can be changed), but the elements must be immutable.
- Sets do not allow duplicate values.

## Creating Sets
```python
my_set = {1, 2, 3}
empty_set = set()  # Correct way to create an empty set
```

## Characteristics
- **Unordered**: No indexing or slicing.
- **Unique Elements**: Duplicates are automatically removed.
- **Mutable Container**: You can add or remove elements.

## Adding Elements
```python
my_set.add(4)  # Adds a single element
my_set.update([5, 6])  # Adds multiple elements
```

## Removing Elements
```python
my_set.remove(2)      # Removes 2; raises KeyError if not found
my_set.discard(10)    # Does not raise an error if element not found
my_set.pop()          # Removes a random element
my_set.clear()        # Empties the set
```

## Set Operations
```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 2}
print(a.symmetric_difference(b)) # {1, 2, 4, 5}
```

## Membership Testing
```python
print(3 in a)  # True
print(10 in a)  # False
```

## Looping Through a Set
```python
for item in a:
    print(item)
```

## Set Comprehension
```python
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
```

## Frozen Sets
- An immutable version of a set.
```python
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # This will raise an error
```
