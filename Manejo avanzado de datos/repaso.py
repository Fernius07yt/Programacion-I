# Tipos de datos 
numero = 1.7
es_viernes = True

# Tipos de datos compuestos
nombre = "Pablo"
lista = [1, 2, 3, 4, 5]

primer_elemento = lista[0] # posiciones válidas: 0 hasta len(lista) - 1
#elemento = lista[12]

for elemento in lista:
    print(elemento)

for letra in nombre:
    print(letra)

if ("a" in nombre):
    print("contiene la a")

temperatura = 36.3

if (temperatura < 37.2):
    print("No tengo fiebre")

# range(inicio=0, final, salto=1) -> 
# genera un rango que incluye el inicio, pero no el final: [inicio, final)
suma = 0
for i in range(7):
    suma = suma + i

def sumatorio (a, b):
    resultado = 0

    for i in range(a, b+1):
        resultado = resultado + i

    return resultado

def multiplicar (a, b):
    resultado = 1

    for i in range(a, b+1):
        resultado = resultado * i

    return resultado


# Los 3 tipos de for:

# Típico: for-each

for elemento in lista:
    print(elemento)

# No tan típico: for i in range(4)

for i in range(100):
    print("Hola")

# Posiciones: enumerate

lista = [45, 22, 56, 111, 342]
resultado = []

for pos, elemento in enumerate(lista):
    if (pos == 0):
        pass
    else:
        resultado.append(elemento)

pos = 0
for elemento in lista:
    if (pos == 0):
        pass
    else:
        resultado.append(elemento)
    pos = pos + 1

for i in range(len(lista)):
    print(f"En la posicion {i} está el elemento {lista[i]}")


def es_primo(n):
    resultado = True

    return resultado

for pos, elemento in enumerate(lista):
    if (es_primo(pos)):
        resultado.append(elemento)

# Solicitar la altura de 5 personas por teclado y 
# mostrar la altura máxima, mínima y media.

alturas = [ 157, 187, 168, 191, 172 ]

suma = 0

maxima = alturas[0]
minima = alturas[0]

for a in alturas:
    suma = suma + a

for a in alturas:
    if (a > maxima):
        maxima = a

for a in alturas:
    if (a < minima):
        minima = a 

media = suma / len(alturas)











