#Swap Two Variables: Swap the values of two variables using a temporary variable.

#traditional and clean method 
from  loguru import logger
first_var  = input("Enter Your first variable: ")
second_var = input("Enter Your second variable: ")

temp = first_var
first_var = second_var
second_var = temp

logger.info(f"Your first variable is '{first_var}' and second variable is'{second_var}'")


#quick tuple unpacking method
a = 20 
b = 40
a,b = b,a
print(a,b)