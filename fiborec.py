#write python code to prinnt fibo


def fib(n):
    if n == 1 or n == 2 :
        return n 
    return fib(n-1) + fib(n-2)

k = fib(8)
print(k)