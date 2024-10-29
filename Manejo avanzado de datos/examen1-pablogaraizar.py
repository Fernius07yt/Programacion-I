# Examen parcial 1 de Pablo Garaizar

# Ejercicio1
def es_primo(numero):
    resultado = True

    if (numero <= 1):
        resultado = False
    else:
        for i in range(2, numero):
            if (numero % i == 0):
                resultado = False
                break

    return resultado

print(es_primo(0))
print(es_primo(1))
print(es_primo(2))
print(es_primo(19))
print(es_primo(113))
print(es_primo(121))

# Ejercicio 2
def calcular_potencias(numero):
    resultado = 0

    for i in range(1, numero+1):
        resultado = resultado + i* 2*i 

    return resultado

print(calcular_potencias(3))

def obtener_lista_potencias(lista):
    resultado = []

    for numero in lista:
        calculo = calcular_potencias(numero)
        resultado.append(calculo)

    return resultado

print(obtener_lista_potencias([1, 2, 3]))
print(obtener_lista_potencias([4, 5, 6,7]))

# Ejercicio 3
def cuenta_impares(lista):
    resultado = 0

    for n in lista:
        if (n % 2 != 0):
            resultado = resultado + 1

    return resultado

def mas_impares(lista):
    resultado = lista[0]

    for lis in lista:
        if (cuenta_impares(lis) > cuenta_impares(resultado)):
            resultado = lis

    return resultado

# Ejercicio 4

def filtrado_especial(lista):
    resultado = []

    for pos, n in enumerate(lista):
        if (True):
            resultado.append(n)

    return resultado