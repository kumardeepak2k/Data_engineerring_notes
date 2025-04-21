#1. check_prime(n) – Return True if n is a prime number.

import math

def check_prime(n):    
    if n<2:
        return False
    else:
        for i in range (2,int(math.sqrt(n))+1):
            if n % i == 0:
                return True
            else:
                return False


y = check_prime(878976541)
print(y)