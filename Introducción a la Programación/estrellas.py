def imprimeEstrellas(n:int):
    print("*" * n)

def imprimeEspacios(n:int):
    print(" " * n, end="")

def imprimeEstrellasRango(desde:int, hasta:int):
    for i in range(desde, hasta+1):
        imprimeEstrellas(i)

def imprimeTriangulo(altura:int):
    imprimeEstrellasRango(1, altura)

def imprimePiramide(altura:int):
    for i in range(1, altura+1):
        imprimeEspacios(altura-i)
        imprimeEstrellas(2*i-1)

imprimePiramide(15)
