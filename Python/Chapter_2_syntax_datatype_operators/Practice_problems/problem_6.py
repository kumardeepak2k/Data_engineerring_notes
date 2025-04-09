from loguru import logger
import math

#Area of Shapes: Calculate the area of a circle, rectangle, and triangle based on user input.

shapes = ["circle", "rectangle", "triangle"]
keep_running = True
while keep_running:
    user_shape = input("Enter your shape('circle'/'rectangle'/'triangle'): ").strip().lower()
    if user_shape not in shapes:
        logger.error("Invalid input. Select from the given options")
        continue
    if user_shape == "circle":
        try:
            radi_circle = float(input("Enter radius of your circle(in m): "))
        except ValueError:
            logger.info("Invalid input. Enter a valid radius")
            continue
        area = math.pi*(radi_circle**2)
    elif user_shape == "rectangle":
        try:
            length_of_rect = float(input("Enter length of your rectangle(in m): "))
            breadth_of_rect = float(input("Enter breadth of your rectangle(in m): "))
        except ValueError:
            logger.info("Invalid input. Enter valid numbers")
            continue
        area = length_of_rect*breadth_of_rect
    
    else:
        try:
            base_of_tri = float(input("Enter base of your triangle(in m): "))
            height_of_tri = float(input("Enter height of your triangle(in m): "))
        except ValueError:
            logger.error("Invalid input. Enter valid numbers") 
            continue
        area = 0.5*base_of_tri*height_of_tri
    
    logger.info(f"The area of {user_shape} is {area:.2f} m²")
    
    user_input = input("Do you want to continue(Yes/No): ").strip().lower()
    if user_input == "no":
        logger.info("Thank you for using the calculator. Goodbye!")
        keep_running = False
    else:
        user_input != "yes"
        logger.error("Invalid response. Exiting program for safety.")
        keep_running = False



