import random

def generar_numeros(n:int) -> list:
    numeros:list = []
    for _ in range(n):
        aleatorio:int = random.randint(1, 1000)
        numeros = numeros + [aleatorio]
    return numeros

def menor(lista:list) -> int:
    candidato:int = lista[0]
    for numero in lista:
        if (numero < candidato):
            candidato = numero
    return candidato

def mayor(lista:list) -> int:
    candidato:int = lista[0]
    for numero in lista:
        if (numero > candidato):
            candidato = numero
    return candidato

def rango(lista:list) -> int:
    return mayor(lista) - menor(lista)

# Programa principal
numeros:list = generar_numeros(100)
print(f"Rango: {rango(numeros)} ({menor(numeros)} - {mayor(numeros)})")