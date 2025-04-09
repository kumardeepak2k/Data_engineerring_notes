from loguru import logger

#Simple Calculator: Ask user for two numbers and an operator (+, -, *, /, //, %, **) and return the result.

operator_list = ['+', '-', '*', '/', '//', '%', '**']

keep_running = True

while keep_running:
    try:
        first_num = float(input("Enter Your first number:"))
        second_num = float(input("Enter Your second number:")) 
    except ValueError:
        logger.error("Invalid input. Enter valid number")
        continue
    
    while True:
        operator = input("Enter operator (+, -, *, /, //, %, **): ").strip()
        if operator not in operator_list:
            logger.error("Invalid Operator. Choose from (+, -, *, /, //, %, **) ")
        else:
            break
    
    if operator == "+":
        result = first_num + second_num
    elif operator == "-":
        result = first_num-second_num
    elif operator == "*":
        result = first_num*second_num
    elif operator == "%":
        result = first_num%second_num
    elif operator == "**":
        result = first_num**second_num
    elif operator == "/":
        if second_num == 0:
            logger.error("Division by zero is not allowed.")
            continue
        result = first_num / second_num
    elif operator == "//":
        if second_num == 0:
            logger.error("Floor division by zero is not allowed.")
            continue
        result = first_num // second_num
    logger.info(f"The value is {result}")

    
    while True:
        user = input("Do you want to exit (Yes/No): ").strip().lower()
        if user == "yes":
            keep_running = False
            break
        elif user =="no":
            break
        else:
            logger.error("Invalid input. Please choose betwen Yes and No")