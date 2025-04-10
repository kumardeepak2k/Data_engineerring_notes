#1.	Count Vowels: Count the number of vowels in a given string.
from loguru import logger

vowels = ["a","e","i", "o","u"]

while True:
    user_input = input("Enter your string: ").lower()
    count = 0
    for char in user_input:
        if char in vowels:
            count += 1
    logger.info(f"The number of vowels in {user_input} is {count}.")

    user = input("Do you want to continue?").strip().lower()
    if user == "no":
        break
    elif user != "yes":
        logger.error("Invalid input")




   

