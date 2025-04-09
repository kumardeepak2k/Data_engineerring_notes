from loguru import logger


#BMI Calculator: Take height and weight from the user and calculate their BMI.




while True:
    try:
        user_height = float(input("Enter your height(in metres): "))
        user_weight = float(input("Enter your Weigth(in kilograms ): "))
    except ValueError:
        logger.error("Invalid input. Enter values again")

    if user_height < 0 or user_weight < 0 :
        logger.error("Values cannot be less than 0 ")
        continue
   
    BMI = user_weight/ (user_height**2)
    logger.info(f"Your BMI is {BMI}")

    
    user = input("Do you want to continue(Yes/NO): ").strip().lower()
    if user == "yes":
        pass
    elif user =="no":
        break
    else:
        logger.error("Invalid input")