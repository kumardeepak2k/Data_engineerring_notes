
# Python Notes - Lists Chapter

## 1. What is a List?
- A list is a mutable (changeable) ordered collection of items.
- Lists are written as comma-separated values enclosed in square brackets `[]`.
  
  Example:
  ```python
  fruits = ["apple", "banana", "cherry"]
  ```

## 2. Creating Lists
- Lists can contain different types of data: strings, integers, floats, or even other lists.

  Example:
  ```python
  mixed_list = [1, 2.5, "hello", True, [1, 2]]
  ```

## 3. Accessing List Elements
- Access list elements by their index, starting from `0`.

  Example:
  ```python
  fruits = ["apple", "banana", "cherry"]
  print(fruits[0])  # Output: apple
  ```

## 4. List Slicing
- You can access a part of the list using slicing.
  - Syntax: `list[start:stop:step]`

  Example:
  ```python
  fruits = ["apple", "banana", "cherry", "date", "elderberry"]
  print(fruits[1:4])  # Output: ['banana', 'cherry', 'date']
  print(fruits[:3])   # Output: ['apple', 'banana', 'cherry']
  print(fruits[::2])  # Output: ['apple', 'cherry', 'elderberry']
  ```

## 5. Modifying Lists
- You can modify elements by directly accessing them using their index.

  Example:
  ```python
  fruits = ["apple", "banana", "cherry"]
  fruits[1] = "blueberry"
  print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
  ```

## 6. List Methods
- Lists have several useful methods:
  - `append(x)`: Adds an item `x` to the end of the list.
  - `insert(i, x)`: Inserts an item `x` at position `i`.
  - `remove(x)`: Removes the first occurrence of item `x`.
  - `pop(i)`: Removes and returns the item at position `i`.
  - `extend(iterable)`: Extends the list by appending elements from an iterable (e.g., another list).
  - `sort()`: Sorts the list in ascending order.
  - `reverse()`: Reverses the elements of the list in place.

  Examples:
  ```python
  fruits = ["apple", "banana", "cherry"]
  
  # Append
  fruits.append("date")
  print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
  
  # Insert
  fruits.insert(1, "blueberry")
  print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'date']
  
  # Remove
  fruits.remove("banana")
  print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']
  
  # Pop
  popped_item = fruits.pop(2)
  print(popped_item)  # Output: 'cherry'
  print(fruits)  # Output: ['apple', 'blueberry', 'date']
  
  # Extend
  fruits.extend(["elderberry", "fig"])
  print(fruits)  # Output: ['apple', 'blueberry', 'date', 'elderberry', 'fig']
  
  # Sort
  fruits.sort()
  print(fruits)  # Output: ['apple', 'blueberry', 'date', 'elderberry', 'fig']
  
  # Reverse
  fruits.reverse()
  print(fruits)  # Output: ['fig', 'elderberry', 'date', 'blueberry', 'apple']
  ```

## 7. List Comprehension
- A concise way to create lists.
  - Syntax: `[expression for item in iterable if condition]`

  Example:
  ```python
  numbers = [1, 2, 3, 4, 5]
  squares = [x**2 for x in numbers]
  print(squares)  # Output: [1, 4, 9, 16, 25]
  
  # List comprehension with condition
  even_squares = [x**2 for x in numbers if x % 2 == 0]
  print(even_squares)  # Output: [4, 16]
  ```

## 8. Nested Lists
- Lists can contain other lists, which are called nested lists.

  Example:
  ```python
  nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print(nested_list[0])  # Output: [1, 2, 3]
  print(nested_list[1][2])  # Output: 6
  ```

## 9. Common List Operations
- **Length of List**: `len(list)`
- **Check if Item Exists**: `item in list`
- **Index of Item**: `list.index(item)`
- **Count Occurrences**: `list.count(item)`
- **Clear the List**: `list.clear()`

  Example:
  ```python
  fruits = ["apple", "banana", "cherry", "apple"]
  
  # Length
  print(len(fruits))  # Output: 4
  
  # Check if Item Exists
  print("apple" in fruits)  # Output: True
  
  # Index of Item
  print(fruits.index("banana"))  # Output: 1
  
  # Count Occurrences
  print(fruits.count("apple"))  # Output: 2
  
  # Clear List
  fruits.clear()
  print(fruits)  # Output: []
  ```

