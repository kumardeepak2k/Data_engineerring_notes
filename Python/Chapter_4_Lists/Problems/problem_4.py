#Second Largest: Find the second largest number in a list.


a = [2, 4, 100, 45, 99, 100, 87]

# Step 1: Remove duplicates
unique_elements = list(set(a))

# Step 2: Check if at least 2 unique elements exist
if len(unique_elements) < 2:
    print("No second largest element exists.")
else:
    # Step 3: Sort in descending order
    unique_elements.sort(reverse=True)
    
    # Step 4: Second largest is at index 1
    second_largest = unique_elements[1]
    print("Second Largest:", second_largest)

max_value = second_max_value = float("-inf")

for num in a:
    if num > max_value:
        second_max_value = max_value
        max_value = num
    elif max_value > num > second_max_value:
        second_max_value = num
        
print(second_max_value)

