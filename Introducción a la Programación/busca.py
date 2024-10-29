import random

# Genera 100 números aleatorios entre 1 y 1000 y guárdalos en una lista.
numeros:list = []

for _ in range(100):
    # generar un número random entre 1 y 1000
    aleatorio:int = random.randint(1, 1000)
    # guardarlo en lista: numeros.append(aleatorio)
    numeros = numeros + [aleatorio]

# Busca el número 37 dentro de la lista

# Si no nos importara la posición, podríamos hacer esto:
for numero in numeros:
    if (numero == 37):
        print("El número 37 está dentro de la lista")
        break

# Como nos interesa saber en qué posición está, tenemos que usar este for:
encontrado:bool = False

for i in range(len(numeros)):
    if (numeros[i] == 37):
        # e indica en qué posición está 
        print(f"El número 37 está dentro de la lista, en la posición {i}")
        encontrado = True
        break

# (si no está, indícalo):
if (encontrado == False):
    print("El número 37 no está en la lista")    
