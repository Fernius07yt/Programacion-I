import random

# Crear matrices

def crear_matriz(filas, cols):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(cols):
            aleatorio = random.randint(1, 10)
            fila.append(aleatorio)
        matriz.append(fila)
    return matriz

a = crear_matriz(2, 2)

print(a)

# Sumatorio
def suma_elementos(matriz):
    resultado = 0

    for fila in matriz:
        for elemento in fila:
            resultado = resultado + elemento

    return resultado

print(suma_elementos(a))

# Producto
def multiplica_elementos(matriz):
    resultado = 1

    for fila in matriz:
        for elemento in fila:
            resultado = resultado * elemento

    return resultado

print(multiplica_elementos(a))

# Filtrar valores
def filtrar_elemento(matriz, k):
    resultado = []

    for fila in matriz:
        f = []
        for elemento in fila:
            if (elemento != k):
                f.append(elemento)
        resultado.append(f)

    return resultado

# Mayor
def mayor_elemento(matriz):
    resultado = matriz[0][0]

    for fila in matriz:
        for elemento in fila:
            if (elemento > resultado):
                resultado = elemento

    return resultado

# Copiar mas grande
def copiar_mas_grande(matriz, k):
    resultado = []

    for fila in matriz:
        f = []
        for elemento in fila:
            if (elemento > k):
                f.append(elemento)
        resultado.append(f)

    return resultado
