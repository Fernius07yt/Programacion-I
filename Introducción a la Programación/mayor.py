import random

# Genera 100 números aleatorios entre 1 y 1000 y guárdalos en una lista.
numeros:list = []

for _ in range(100):
    # generar un número random entre 1 y 1000
    aleatorio:int = random.randint(1, 1000)
    # guardarlo en lista: numeros.append(aleatorio)
    numeros = numeros + [aleatorio]

# Buscar el número mayor si no nos interesa su posición
mayor:int = numeros[0]

for numero in numeros:
    if (numero > mayor):
        mayor = numero

print(f"El número mayor de la lista es {mayor}")

# Buscar el número mayor si nos interesa su posición
mayor:int = numeros[0]
posicion:int = 0

for i in range(len(numeros)):
    if (numeros[i] > mayor):
        mayor = numeros[i]
        posicion = i

print(f"El número mayor de la lista es {mayor} y estaba en la posición {posicion}")
