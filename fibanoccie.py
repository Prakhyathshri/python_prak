def fib(n):
    if (n==0):
        return 0
    elif (n==1):   
        return 1
    else:
        return fib(n-1) + fib(n-2) 

print(fib(5))
print(fib(4))
print(fib(3))
print(fib(2))
print(fib(1))
print(fib(0))

# formula of fibbonacci series is ( num - 1 ) + ( num - 2)