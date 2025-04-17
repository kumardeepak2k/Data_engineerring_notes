#Set Comprehension Challenge
# Create a set of all square numbers less than 100 that are divisible by 4 using set comprehension.


squaredlist = { x**2 for x in range(1,10) if (x**2)%4 == 0}
print(squaredlist)