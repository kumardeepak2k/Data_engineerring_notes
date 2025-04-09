from loguru import logger

#Check Valid Triangle: Given 3 sides, check if a triangle is valid using triangle inequality rules

keep_running = True

while True:
    sides =[]
    all_valid = True
    try:
        for i in range(3):
            user_input = float(input(f"Enter length of side{i+1}(in cm)"))
            if user_input < 0:
                all_valid = False
                break
            else:
                sides.append(user_input)
    except ValueError:
        logger.error("Invalid Input")
        all_valid = False
    if all_valid:
        break
print (sides)


    