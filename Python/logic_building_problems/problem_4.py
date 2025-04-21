# #4. sum_of_digits(n) – Return the sum of all digits of a number.

# #string typecasting
# def sum_of_digits(n):
#     total = 0 
#     for char in str(n):
#         total += int(char)
#     return total


# print(sum_of_digits(53435))

#math logic

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10 
        n = n//10
    return total

print(sum_of_digits(352525))