# Even or Odd: Check if a number is even or odd using the modulo operator.
from loguru import logger

keep_running = True

while keep_running:
    
    try:
        num = int(input("Enter Your integer: "))
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        logger.error("Invalid input. Enter an integer")
    
    while True:
        user = input("Do you want to Exit (Yes/No): ").strip().lower()
        if user == "yes":
            keep_running = False
            break
        elif user == "no":
            break
        else:
            logger.error("Invalid input. Please choose between Yes and NO")
            continue


