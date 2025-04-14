# Creating markdown notes for Python Sets
set_notes = """
# Python Sets 🧩

Sets are **unordered**, **unindexed**, and contain **unique elements only**.

---

## 📌 Key Characteristics:
- Defined using `{}` or `set()`.
- Unordered: No indexing or slicing.
- Mutable: Can add or remove elements.
- No duplicate values allowed.

---

## 🛠️ Creating Sets:

```python
s1 = {1, 2, 3}
s2 = set([4, 5, 6])
✅ Basic Operations:
python
Always show details

Copy
s = {1, 2, 3}
print(2 in s)       # True
print(len(s))       # 3
➕ Adding Elements:
python
Always show details

Copy
s.add(4)  # Add single element
s.update([5, 6])  # Add multiple elements
➖ Removing Elements:
python
Always show details

Copy
s.remove(3)    # Raises error if not found
s.discard(10)  # Does not raise error
s.pop()        # Removes random element
s.clear()      # Empties the set
🔁 Looping Through Set:
python
Always show details

Copy
for item in s:
    print(item)
📚 Set Operations:
python
Always show details

Copy
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)         # {1, 2, 3, 4, 5}
a | b              # same as union

a.intersection(b)  # {3}
a & b              # same as intersection

a.difference(b)    # {1, 2}
a - b              # same as difference

a.symmetric_difference(b)  # {1, 2, 4, 5}
a ^ b
✅ Set Comparisons:
python
Always show details

Copy
a == b       # Checks if sets are equal
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)
⚠️ Important Notes:
Sets do not allow mutable elements like lists or other sets.

Frozen sets: Immutable version of a set.

python
Always show details

Copy
fset = frozenset([1, 2, 3])
💡 Use Cases:
Removing duplicates from a list.

Fast membership tests.

Mathematical set operations (union, intersection, etc.)

🧪 Practice:
Remove duplicates from a list using set.

Count the number of unique elements in a list.

Find common elements in two lists using set.

Check if a list is a subset of another.