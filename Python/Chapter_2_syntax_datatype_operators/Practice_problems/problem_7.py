#Compare Three Numbers: Take three numbers and print the largest using logical operators.
from loguru import logger


keep_running = True

while keep_running:
    try:
        first_num = float(input("Enter Your First Number: "))
        second_num = float(input("Enter Your Second Number: "))
        third_num = float(input("Enter Your Third Number: "))
    
    except ValueError:
        logger.error("Invalid Number. Enter valid numbers")
        continue

    if first_num >= second_num and first_num >= third_num:
        logger.info(f"{first_num} is the largest number")
    elif second_num >= first_num and second_num >= third_num:
        logger.info(f"{second_num} is the largest number")
    else:
        logger.info(f"{third_num} is the largest number")

    user = input("Do you want to continue(Yes/No): ").strip().lower()
    if user == "yes":
        pass
    elif user == "no":
        keep_running = False
    else:
        logger.error("Invalid entry. Choose between 'Yes' and 'No' ")

