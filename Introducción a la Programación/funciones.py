# Función suma
def suma(a:int, b:int):
    resultado = a + b
    return resultado

# Función mayor(a, b) que devuelve a si a > b o devuelve b si b > a
def mayor(a:int, b:int):
    if (a > b):
        return a
    else:
        return b

# Otra función mayor, pero con un solo return
def mayor2(a:int, b:int):
    resultado = 0
    if (a > b):
        resultado = a
    else:
        resultado = b
    return resultado

# Funcion factorial
def factorial (n:int):
    resultado = 1
    for i in range(1, n+1):
        resultado = resultado * i
    return resultado

# Programa principal (no está dentro de una función)
print(factorial(100))
print(f"50! = {factorial(50)}")
print(f"100! = {factorial(100)}")
print(f"200! = {factorial(200)}")