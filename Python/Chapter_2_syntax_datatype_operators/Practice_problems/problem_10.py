from loguru import logger

#Check Valid Triangle: Given 3 sides, check if a triangle is valid using triangle inequality rules

# keep_running = True

keep_running = True
while keep_running:
    sides = []
    all_valid = True
    try:
        for i in range(3):
            user_input = int(input("Enter length of side {i+1} (in cm): "))
            if user_input < 0:
                logger.error("Invalid input. Length can not be negative")
                all_valid = False
                break
            else:
                sides.append(user_input)
    except:
            logger.error("Invalid Entry. Select a number")
            break

    if all_valid:
        a,b,c = sides
        if (a+b>c) and (a+c>b) and (b+c>a):
            logger.info("Valid triangle with Sides:")
        else:
            logger.info("Not a valid triangle")
    else:
        logger.info("Invalid Entry")


    repeat = input("Do you want to try again? ").strip().lower()
    if repeat == 'yes':
        pass
    elif repeat == 'no':
        keep_running = False
    else:
        logger.info("Invalid Entry")

        

    

        
            

    