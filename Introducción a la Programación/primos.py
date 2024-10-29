def esPrimo(n:int) -> bool:
    resultado:bool = True
    for i in range(2, n):
        if (n % i == 0):
            resultado = False
            break
    return resultado

print(esPrimo(7))
print(esPrimo(8))