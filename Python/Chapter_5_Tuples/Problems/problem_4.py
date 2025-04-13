#4.	Tuple of Squares: Generate a tuple of squares for numbers from 1 to n.
try:
    n = int(input("Enter Your Number: "))
except ValueError:
    print("Invalid Input")

squared_tuple = tuple([i**2 for i in range(1,n+1)])
print(squared_tuple)