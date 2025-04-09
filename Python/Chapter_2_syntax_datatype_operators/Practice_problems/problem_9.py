from loguru import logger

#Leap Year Checker: Ask for a year and determine whether it’s a leap year using logical conditions.

Keep_running = True

while Keep_running:
    try:
        user_year = int(input("Enter year(e.g.2024): "))
        if user_year < 1000:
            logger.error("Enter year greater than 1000(e.g. 2024)")
            continue
        if (user_year % 4 ==0 and user_year % 100 != 0) or user_year % 400 == 0:
                logger.info(f"{user_year} is a leap year")
        else:
            logger.info(f"{user_year} is not a leap year")
    except ValueError:
        logger.error("Invalid input. Enter a valid year")
    
    user_input = input("Do you want to exit(Yes/No): ").strip().lower()
    if user_input == "yes":
        logger.info("Thank you for using Leap Checker")
        Keep_running = False
    elif user_input == "no":
        pass
    else:
        logger.error("Invalid input. Exiting for Safety")
        Keep_running = False
