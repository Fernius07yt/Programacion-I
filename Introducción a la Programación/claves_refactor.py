import random

def clave(n:int, alfabeto:str) -> str:
    resultado:str = ""
    for _ in range(n):
        aleatorio:int = random.randint(0, len(alfabeto) - 1)
        letra:str = alfabeto[aleatorio]
        resultado = resultado + letra
    return resultado

def clavenum(n:int) -> str:
    return clave(n, "0123456789")

def clavealfa(n:int) -> str:
    return clave(n, "abcdefghijklmnopqrstuvwxyz")

def clavefuerte(n:int) -> str:
    return clave(n , "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]_ !@-#")

print(clavenum(4))
print(clavenum(7))
print(clavealfa(4))
print(clavealfa(7))
print(clavefuerte(12))