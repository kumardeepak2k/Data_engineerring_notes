
# 🧵Chapter: Strings

---

## ✅ 1. What is a String?

- A **string** is a sequence of **Unicode characters** in Python.
- Strings are **immutable** — cannot be changed after creation.
- Created using:
  - `'single quotes'`
  - `"double quotes"`
  - `'''triple quotes'''` or `"""triple quotes"""` for multi-line strings

```python
s1 = 'hello'
s2 = "world"
s3 = '''multi
line'''
```

---

## ✅ 2. String Indexing & Slicing

- **Indexing**: `s[index]` — zero-based, negative index from end
- **Slicing**: `s[start:end:step]` — end is **exclusive**

```python
s = "Deepak"
print(s[0])    # D
print(s[-1])   # k
print(s[1:4])  # eep
print(s[::-1]) # kapeeD (reversed)
```

---

## ✅ 3. String Immutability

- Strings can't be modified directly

```python
s = "deepak"
# s[0] = 'D'  ❌ Error
s = "D" + s[1:]  # ✅ Correct
```

---

## ✅ 4. Useful String Methods

### 🔹 Case Conversion

```python
s.lower()        # all lowercase
s.upper()        # all uppercase
s.title()        # Title Case
s.capitalize()   # First letter uppercase
s.swapcase()     # Swap upper/lower
```

### 🔹 Search & Check

```python
s.find('a')         # index or -1
s.index('a')        # like find() but raises error
s.startswith('De')  # True
s.endswith('ak')    # True
```

### 🔹 Validation (Boolean)

```python
s.isalpha()     # letters only
s.isdigit()     # digits only
s.isalnum()     # letters + digits
s.isspace()     # whitespace only
s.islower()     # all lowercase
s.isupper()     # all uppercase
```

### 🔹 Modification

```python
s.replace('a', 'x')     # replaces 'a' with 'x'
s.strip()               # removes both-side spaces
s.lstrip(), s.rstrip()  # left/right strip
s.split(' ')            # split into list
' '.join(list)          # join list into string
```

---

## ✅ 5. String Formatting

### 🔹 f-Strings (Recommended)

```python
name = "Deepak"
age = 24
print(f"My name is {name} and I am {age} years old.")
```

### 🔹 format()

```python
print("My name is {} and I am {} years old.".format(name, age))
```

### 🔹 % Formatting (Old Style)

```python
print("My name is %s and I am %d years old." % (name, age))
```

---

## ✅ 6. String Comparisons

```python
'apple' < 'banana'   # True
'abc' == 'ABC'       # False
```

---

## ✅ 7. Escape Characters

| Escape | Meaning        |
|--------|----------------|
| `\n`   | New Line       |
| `\t`   | Tab            |
| `\\`  | Backslash      |
| `\'`   | Single quote   |
| `\"`  | Double quote   |

```python
print("Hello\nWorld")
print("He said, \"Hi\"")
```

---

## ✅ 8. Iteration & Membership

```python
for char in "Deepak":
    print(char)

'd' in "Deepak"       # True
'z' not in "Deepak"   # True
```

---

## ✅ 9. ASCII Conversion

```python
ord('A')   # 65
chr(65)    # 'A'
```

---
