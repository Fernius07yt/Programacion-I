def fact(n: int) -> int:
    resultado:int = 1
    for i in range(1, n+1):
        resultado = resultado * i
    return resultado

def factorial(n: int) -> int:
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
    
def fib(n:int) -> int:
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fact(10))
print(factorial(10))
print(fib(10))