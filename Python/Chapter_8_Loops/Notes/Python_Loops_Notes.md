
# Python Loops

In Python, loops are used to iterate over a sequence (such as a list, tuple, dictionary, string, or range) and execute a block of code repeatedly.

## 1. For Loop
A `for` loop is used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in the sequence.

### Syntax:
```python
for item in iterable:
    # Do something with item
```

### Example:
```python
for i in range(5):
    print(i)
```
**Output:**
```
0
1
2
3
4
```

- The loop iterates over the sequence produced by `range(5)` and prints each value.
- You can loop over any iterable object like a list, string, or dictionary.

## 2. While Loop
A `while` loop is used to repeatedly execute a block of code as long as the specified condition is `True`.

### Syntax:
```python
while condition:
    # Do something while the condition is True
```

### Example:
```python
i = 0
while i < 5:
    print(i)
    i += 1
```
**Output:**
```
0
1
2
3
4
```

- The loop continues as long as `i` is less than 5, incrementing `i` after each iteration.

## 3. Nested Loops
You can use one loop inside another. This is called a **nested loop**.

### Example:
```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```
**Output:**
```
i: 0, j: 0
i: 0, j: 1
i: 1, j: 0
i: 1, j: 1
i: 2, j: 0
i: 2, j: 1
```

- In this example, the outer loop runs 3 times, and the inner loop runs 2 times for each outer loop iteration.

## 4. Loop Control Statements

### a) Break
The `break` statement is used to exit the loop prematurely.

### Example:
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```
**Output:**
```
0
1
2
```
- The loop breaks when `i` is equal to 3, exiting the loop.

### b) Continue
The `continue` statement is used to skip the current iteration and continue with the next iteration of the loop.

### Example:
```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```
**Output:**
```
0
1
2
4
```
- When `i` is 3, the `continue` statement skips the rest of the code inside the loop for that iteration.

### c) Else with Loop
An `else` block can be used after a loop to specify code that runs if the loop completes normally (i.e., it doesn’t hit a `break`).

### Example:
```python
for i in range(5):
    print(i)
else:
    print("Loop completed successfully.")
```
**Output:**
```
0
1
2
3
4
Loop completed successfully.
```

## 5. Looping Through Different Data Structures

### a) List:
```python
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)
```

### b) String:
```python
my_string = "Python"
for char in my_string:
    print(char)
```

### c) Dictionary:
You can loop through a dictionary using `keys()`, `values()`, or `items()`.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)
```

## Conclusion
- `for` loops are ideal for iterating over a sequence.
- `while` loops are ideal for repeating an action as long as a condition holds.
- Loop control statements like `break`, `continue`, and `else` allow more control over the flow of the loop.
- Nested loops allow complex looping structures for multi-dimensional data.

