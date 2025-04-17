#Number Guessing Game: Write a loop that asks the user to guess a number until they guess it right.
#  Give hints like "Too high" or "Too low".

#my code 
keep_running = True
num = 45

while keep_running:
    try:
        user_input = int(input("Enter Your Number(1-100): "))
    except ValueError:
        print("Invalid input. Enter a valid number(1-100): ")
    
    if user_input > num:
        print("Guess lower")
    elif user_input < num:
        print("Guess higher")
    else:
        print("Correct Guess....")
    
    user_i = input(" Do you want to play again(Yes/No): ").strip().lower()
    if user_i == "no":
        keep_running = False
    elif user_i != "yes":
        print("Invalid input. Choose between Yes or No")


#chatgpt logic
keep_running = True
num = 45
max_attempts = 5

while keep_running:
    attempts = 0  # To track the number of guesses
    
    while attempts < max_attempts:
        try:
            user_input = int(input(f"Enter Your Number (1-100): "))
            
            if user_input < 1 or user_input > 100:
                print("Please choose a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number (1-100).")
            continue
        
        attempts += 1
        
        if user_input > num:
            print("Guess lower!")
        elif user_input < num:
            print("Guess higher!")
        else:
            print(f"Correct guess! Well done! It took you {attempts} attempts.")
            break  # Exit the loop if the guess is correct
        
        # If maximum attempts are reached
        if attempts == max_attempts:
            print(f"You've used all {max_attempts} attempts. The correct number was {num}.")
    
    # Ask if the user wants to play again
    user_i = input("Do you want to play again? (Yes/No): ").strip().lower()
    
    if user_i == "no":
        keep_running = False
    elif user_i != "yes":
        print("Invalid input. Please choose between 'Yes' or 'No'.")



