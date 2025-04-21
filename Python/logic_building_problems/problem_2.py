#2. fibonacci(n) – Return the first n terms of the Fibonacci series as a list.


def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]

    fib_seq = [0,1]
    for i in range(2,n):
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)
    
    return fib_seq

y = fibonacci(45)
print(y)
     