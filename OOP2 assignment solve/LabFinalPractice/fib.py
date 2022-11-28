def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)
    
for i in range(int(input())):
    n = int(input())
    print(f'Fibonacci({n}) = {Fibonacci(n)}')
    n= 0