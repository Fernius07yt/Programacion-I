def multiplo(a: int, b: int) -> bool:
    """solicita dos números y devuelve si el primero es múltiplo del segundo o no"""
    resultado:bool = False
    if (a % b == 0):
        resultado = True
    return resultado

def impares() -> list:
    """devuelve todos los números impares desde 1 hasta 99"""
    resultado:list = []
    for i in range(1, 100, 2):
        resultado = resultado + [i]
    return resultado

def fecha_correcta(dia:int, mes:int, anno:int) -> bool:
    """devuelve True si la fecha es correcta (el día está entre 1 y 31, el mes está entre 1 y 12, etc.). """
    resultado:bool = True
    if ( (mes < 1 or mes > 12) or (dia < 1 or dia > 31) ):
        resultado = False
    return resultado

def anno_bisiesto(anno:int) -> bool:
    """devuelve True si el anno es bisiesto"""
    resultado:bool = False
    if ( (anno % 400 == 0) or (anno % 4 == 0 and anno % 100 != 0) ):
        resultado = True
    return resultado

print(anno_bisiesto(2100))

def ordenar(a:int, b:int, c:int) -> list:
    """devuelve una lista con los números a, b y c ordenados de menor a mayor"""
    resultado:list = []
    if (a <= b and a <= c):
        # a es el menor
        if (b <= c):
            resultado = [a, b, c]
        else:
            resultado = [a, c, b]
    elif (b <= a and b <= c):
        # b es el menor
        if (a <= c):
            resultado = [b, a, c]
        else:
            resultado = [b, c, a]
    else:
        # c es el menor
        if (a <= b):
            resultado = [c, a, b]
        else:
            resultado = [c, b, a]
    return resultado

def ordenar2(a:int, b:int, c:int) -> list:
    """devuelve una lista con los números a, b y c ordenados de menor a mayor"""
    resultado:list = [a,b,c]
    resultado.sort()
    return resultado
