import random

def clavenum(n:int) -> str:
    resultado:str = ""
    for _ in range(n):
        aleatorio:int = random.randint(0, 9)
        resultado = resultado + str(aleatorio)
    return resultado

def clavealfa(n:int) -> str:
    resultado:str = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(n):
        aleatorio:int = random.randint(0, len(alfabeto) - 1)
        letra:str = alfabeto[aleatorio]
        resultado = resultado + letra
    return resultado

def clavefuerte(n:int) -> str:
    resultado:str = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]_ !@-#"
    for _ in range(n):
        aleatorio:int = random.randint(0, len(alfabeto) - 1)
        letra:str = alfabeto[aleatorio]
        resultado = resultado + letra
    return resultado


print(clavenum(4))
print(clavenum(7))
print(clavealfa(4))
print(clavealfa(7))
print(clavefuerte(12))