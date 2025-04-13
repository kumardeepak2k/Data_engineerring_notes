#8.	Nested Tuple Operations: Work with nested tuples like ((1, 2), (3, 4)) and sum all values.

a =  ((1, 2), 5,(3, (9,8)))

stack = [a]
sum = 0
while stack:
    current = stack.pop()
    if isinstance(current, int):
        sum += current
    elif isinstance(current,(tuple,list)):
        stack.extend(current)
print(sum)