# Funcion que calcula el factorial del número que recibe
# recibe: n (número)
# devuelve = n! (número)
def factorial(n):
    resultado = 1

    for i in range(1, n+1):
        resultado = resultado * i
        
    return resultado

# Funcion que calcula el sumatorio desde 1 hasta n
# recibe: n (numero)
# devuelve: el sumatorio (numero)
def sumatorio(n):
    resultado = 0

    for i in range(1, n+1):
        resultado = resultado + i
        
    return resultado

def primera_letra(frase):
    resultado = frase[0]
    return resultado

def ultima_letra(frase):
    resultado = frase[-1]
    return resultado

print(factorial(5))
print(factorial(120))
print(sumatorio(10))