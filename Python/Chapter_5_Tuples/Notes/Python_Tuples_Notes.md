
# Python Chapter: Tuples

## 📌 Introduction to Tuples
- A **tuple** is an immutable, ordered collection of elements.
- Defined using **parentheses ()**.
- Elements can be of different data types.
- Once created, the values **cannot be changed** (unlike lists).

```python
tuple1 = (1, 2, 3)
tuple2 = ('apple', 'banana', 'cherry')
```

---

## ✅ Properties of Tuples
| Property        | Description                          |
|----------------|--------------------------------------|
| Ordered        | Maintains the order of elements      |
| Immutable      | Cannot be changed after creation     |
| Heterogeneous  | Can store multiple data types        |
| Iterable       | Can be looped through                |

---

## 🧱 Creating Tuples
```python
# Empty tuple
t = ()

# Tuple with one element (requires comma)
t = (5,)

# Tuple with multiple elements
t = (1, 'a', 3.5)
```

---

## 🌀 Accessing Elements
```python
t = (10, 20, 30)
print(t[0])  # Output: 10
print(t[-1]) # Output: 30
```

---

## 🧭 Tuple Slicing
```python
t = (0, 1, 2, 3, 4, 5)
print(t[1:4])  # Output: (1, 2, 3)
print(t[:3])   # Output: (0, 1, 2)
```

---

## 🧪 Tuple Methods
Tuples have only **two built-in methods**:
```python
t = (1, 2, 3, 2, 1)
print(t.count(2))  # Output: 2
print(t.index(3))  # Output: 2
```

---

## 🧲 Tuple Operations
```python
# Concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # Output: (1, 2, 3, 4)

# Repetition
t = (1, 2)
print(t * 3)    # Output: (1, 2, 1, 2, 1, 2)
```

---

## ♻️ Tuple vs List
| Feature         | List         | Tuple        |
|----------------|--------------|--------------|
| Syntax         | [1, 2, 3]     | (1, 2, 3)     |
| Mutable        | Yes           | No           |
| Methods        | Many          | Few          |
| Performance    | Slower        | Faster       |
| Use Case       | Dynamic data  | Fixed data   |

---

## 🎯 When to Use Tuples
- When data should not change
- As dictionary keys
- For fixed collections like coordinates, RGB values, etc.

---

## 🧠 Tuple Unpacking
```python
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Output: 1 2 3
```

---

## 🚨 Common Mistakes
```python
# Single element tuple must have a comma
t = (5)     # This is NOT a tuple
print(type(t))  # Output: <class 'int'>

t = (5,)   # Correct tuple with one element
print(type(t))  # Output: <class 'tuple'>
```

---

## 🧩 Practice Questions
1. Create a tuple with numbers from 1 to 5.
2. Check if a value exists in a tuple.
3. Count how many times a number occurs in a tuple.
4. Use tuple unpacking to assign values.
5. Write a function that returns a tuple of min and max values in a list.

---
