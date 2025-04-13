#7.	Convert List to Tuple: Take a list from user and convert it into a tuple.

Keep_running = True
u_list = []  # Initialize an empty list to store user inputs

while Keep_running:
    user_input = input("Enter your elements (type 'done' to stop): ")
    
    if user_input.lower() == "done":  # Exit the loop if the user types 'done'
        Keep_running = False
    else:
        # Check if the input is a valid number (integer or float)
        if user_input.replace('.', '', 1).isdigit() and user_input.count('.') < 2:  # Check for numeric input
            if '.' in user_input:
                u_list.append(float(user_input))  # Convert to float
            else:
                u_list.append(int(user_input))  # Convert to integer
        else:
            u_list.append(user_input)  # If it's not numeric, keep it as a string

# Convert the list to a tuple after the loop ends
user_tuple = tuple(u_list)

# Print the resulting tuple
print(user_tuple)
