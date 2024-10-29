import random

# Genera 100 números aleatorios entre 1 y 1000 y guárdalos en una lista.
numeros:list = []

for _ in range(100):
    # generar un número random entre 1 y 1000
    aleatorio:int = random.randint(1, 1000)
    # guardarlo en lista: numeros.append(aleatorio)
    numeros = numeros + [aleatorio]

# Buscar el número menor en la lista de números
menor:int = numeros[0]

for numero in numeros:
    if (numero < menor):
        menor = numero

print(f"El número menor es {menor}")

# Buscar el número menor en la lista de números pero sabiendo su posición
menor:int = numeros[0]
posicion:int = 0

for i in range(len(numeros)):
    if (numeros[i] < menor):
        menor = numeros[i]
        posicion = i

print(f"El número menor es {menor} y estaba en la posicion {posicion}")

