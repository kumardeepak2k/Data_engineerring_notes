#Add Two Numbers: Take two numbers from the user and print their sum
from loguru import logger

first_num = float(input("Enter Your first Number: "))
second_num = float(input("Enter Your second Number: "))

logger.info(f"The sum of your two numbers is: {first_num +second_num}")

try:
    first_num = float(input("Enter Your first Number: "))
    second_num = float(input("Enter Your second Number: "))
    logger.info(f"The sum of your two numbers is: {first_num +second_num}")

except:
    logger.warning("Invalid input. Enter a valid number")
    print("Enter a valid Number")
