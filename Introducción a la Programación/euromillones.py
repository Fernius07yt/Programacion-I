import random

def jugada() -> list:
    resultado:list = []
    for _ in range(5):
        aleatorio:int = random.randint(1, 50)
        while (aleatorio in resultado):
            aleatorio:int = random.randint(1, 50)
        resultado = resultado + [aleatorio]
    return resultado

def estrellas() -> list:
    resultado:list = []
    
    aleatorio1:int = random.randint(1, 11)
    resultado = resultado + [aleatorio1]
    
    aleatorio2:int = random.randint(1, 11)
    while (aleatorio2 == aleatorio1):
        aleatorio2:int = random.randint(1, 11)
    resultado = resultado + [aleatorio2]
    
    return resultado

print(jugada())
print(estrellas())

"""
Versión REFACTORIZANDO:

def generar(cuantos:int, inicio:int, fin:int) -> list:
    resultado:list = []
    for _ in range(cuantos):
        aleatorio:int = random.randint(inicio, fin)
        while (aleatorio in resultado):
            aleatorio:int = random.randint(inicio, fin)
        resultado = resultado + [aleatorio]
    return resultado

def jugada() -> list:
    return generar(5, 1, 50)

def estrellas() -> list:
    return generar(2, 1, 11)
"""
