# 10.Tuple Merging: Merge multiple tuples into a single flat tuple.


# Define multiple tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple3 = (6, 7, 8)

# Merge the tuples using sum
merged_tuple = sum((tuple1, tuple2, tuple3), ())

print(merged_tuple)

# Define multiple tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple3 = (6, 7, 8)

# Merge the tuples using list comprehension
merged_tuple = tuple([item for t in (tuple1, tuple2, tuple3) for item in t])

print(merged_tuple)


