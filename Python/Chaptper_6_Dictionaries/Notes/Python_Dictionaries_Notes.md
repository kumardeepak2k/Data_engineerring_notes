
# Python Chapter: Dictionaries

## Introduction
- A dictionary in Python is an unordered(prior to 3.7) collection of data in a key:value pair form.
- Dictionaries are mutable and indexed by keys.

## Syntax
```python
my_dict = {
    "name": "Deepak",
    "age": 24,
    "city": "Odisha"
}
```

## Key Features
- Keys are unique and immutable (e.g., strings, numbers, tuples)
- Values can be of any datatype and can repeat

## Accessing Elements
```python
print(my_dict["name"])       # Access using key
print(my_dict.get("age"))    # Access using get() method (returns None if key not found)
```

## Modifying Dictionary
```python
my_dict["age"] = 25          # Update value
my_dict["email"] = "abc@mail.com"  # Add new key-value pair
```

## Removing Elements
```python
del my_dict["city"]          # Removes key 'city'
my_dict.pop("email")         # Removes 'email' and returns its value
my_dict.clear()              # Clears the entire dictionary
```

## Dictionary Methods
| Method        | Description |
|---------------|-------------|
| `get(key)`     | Returns the value for a key if it exists |
| `keys()`       | Returns a view object of all keys |
| `values()`     | Returns a view object of all values |
| `items()`      | Returns a view object of all (key, value) pairs |
| `update()`     | Updates dictionary with elements from another dictionary or iterable |
| `pop(key)`     | Removes key and returns its value |
| `clear()`      | Removes all elements from the dictionary |

## Looping Through Dictionary
```python
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(f"{key}: {value}")
```

## Dictionary Comprehension
```python
squares = {x: x*x for x in range(6)}
print(squares)
```

## Nested Dictionary
```python
student = {
    "name": "Deepak",
    "marks": {
        "math": 90,
        "science": 85
    }
}
print(student["marks"]["science"])
```

## Common Interview Tips
- Understand `get()` vs direct key access.
- Practice nested dictionary access and modifications.
- Use `items()` for looping with both key and value.
