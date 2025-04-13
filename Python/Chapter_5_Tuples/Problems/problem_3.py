#3.	Check Element: Check if a given element exists in a tuple.

my_list = [10] * 10**6 + [30] * 10**3
element_to_check = 99
found = False

for item in my_list:
    if item == element_to_check:
        print(f"Found {element_to_check}")
        found = True
        break

if not found:
    print(f"{element_to_check} not found in the list.")
