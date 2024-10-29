def mayor(a:list, b:list) -> bool:
    """devuelve True si cada elemento de a es mayor que su correspondiente en b"""
    resultado:bool = True
    for i in range(len(a)):
        if (a[i] <= b[i]):
            resultado = False
            break
    return resultado

def empezar_igual(a: list, b: list, n: int) -> bool:
    """devuelve True si los n primeros elementos de a son los mismos que los de b"""
    resultado:bool = True
    for i in range(n):
        if (a[i] != b[i]):
            resultado = False
            break
    return resultado

print(empezar_igual([1,2,3,4,5], [1,2,3,4,6], 3)) # True
print(empezar_igual([1,2,3,4,5], [1,2,3,4,6], 5)) # False

def terminar_igual(a: list, b: list, n: int) -> bool:
    """devuelve True si los n últimos elementos de a son los mismos que los de b"""
    resultado:bool = True
    for i in range(len(a)-1, len(a)-n, -1):
        if (a[i] != b[i]):
            resultado = False
            break
    return resultado

def rima(a:str, b:str, n:int) -> bool:
    """devuelve True si las últimas n letras de a son las mismas que las de b"""
    resultado:bool = True
    for i in range(len(a)-1, len(a)-n, -1):
        if (a[i] != b[i]):
            resultado = False
            break
    return resultado
    #return terminar_igual(list(a), list(b), n)

# No asume que la palabra a es igual de larga que la palabra b
def rima2(a:str, b:str, n:int) -> bool:
    """devuelve True si las últimas n letras de a son las mismas que las de b"""
    resultado:bool = True
    a = a[::-1]
    b = b[::-1]
    for i in range(n):
        if (a[i] != b[i]):
            resultado = False
            break
    return resultado

def dos_junto_a_dos(numeros:list) -> bool:
    resultado:bool = False
    # muy importante este -1 para que no vaya hasta la última posición, sino la penúltima
    for i in range(len(numeros)-1):
        if (numeros[i] == 2 and numeros[i+1] == 2):
            resultado = True
            break
    return resultado

print(rima2("canción", "camión", 2)) # True
print(rima2("canción", "camión", 4)) # False

print(mayor([1,2,3], [0,1,2])) # True
print(mayor([1,2,3], [4,1,2])) # False

def mayor_diferencia(numeros:list) -> int:
    resultado:int = 0
    mayor:int = numeros[0]
    menor:int = numeros[0]
    for n in numeros:
        if (n < menor):
            menor = n
        if (n > mayor):
            mayor = n
    resultado = mayor - menor
    return resultado
    # return max(numeros) - min(numeros)

def suma_digitos(palabra:str) -> int:
    resultado:int = 0
    for letra in palabra:
        if (letra in "0123456789"):
            resultado = resultado + int(letra)
    return resultado

print(suma_digitos("c123a"))

def parsea_entero(palabra:str) -> int:
    resultado:int = 0
    numero:str = ""
    for letra in palabra:
        if (letra in "0123456789"):
            numero = numero + letra
    resultado = int(numero)
    return resultado

def borra_letras(palabra:str, borrar:str) -> str:
    resultado:str = ""
    for letra in palabra:
        if (letra not in borrar):
            resultado = resultado + letra
    return resultado