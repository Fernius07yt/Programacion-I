# Ejercicio 1a
def multiplicar (a, b):
    resultado = 1

    for n in range(a, b+1):
        resultado = resultado * n

    return resultado

# print(multiplicar(1, 3))

# Ejercicio 1b
def factoriales (lista):
    resultado = []

    for n in lista:
        resultado.append(multiplicar(1, n))

    return resultado


# Ejercicio 2
def cuenta_vocales (palabra):
    resultado = 0

    for letra in palabra:
        if (letra in "aeiouAEIOU"):
            resultado = resultado + 1

    return resultado

def mas_vocales (lista):
    resultado = lista[0]

    for palabra in lista:
        if (cuenta_vocales(palabra) > cuenta_vocales(resultado)):
            resultado = palabra

    return resultado

print(mas_vocales(["aceituna", "tomate", "hola"])) # Devuelve "aceituna"

# Ejercicio 3
def es_primo (n):
    resultado = True

    if (n < 2):
        resultado = False
    else:
        for i in range(2, n):
            if (n % i == 0):
                resultado = False
                break

    return resultado    

def posiciones_primas (lista):
    resultado = []

    for pos, elemento in enumerate(lista):
        if (es_primo(pos)):
            resultado.append(elemento)

    return resultado

# Extra
def comprimir_vocales (frase):
    resultado = ""

    anterior = frase[0]
    contador = 1

    for pos, letra in enumerate(frase):
        if (pos != 0):
            if (letra == anterior):
                contador = contador + 1
            else:
                resultado = resultado + str(contador) + anterior
                anterior = letra
                contador = 1

    resultado = resultado + str(contador) + letra

    return resultado
