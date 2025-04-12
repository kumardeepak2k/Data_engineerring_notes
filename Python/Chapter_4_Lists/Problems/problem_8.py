#Flatten Nested List: Flatten a list like [1, [2, 3], [4, [5, 6]]] into [1, 2, 3, 4, 5, 6]

a =  [1, [2, 3], [4, [5, 6]]]
stack = a[::-1]
new = []

while stack:
    end =  stack.pop()
    if isinstance(end,list):
      stack.extend(end[::-1])
    else:
       new.append(end)

print(new)