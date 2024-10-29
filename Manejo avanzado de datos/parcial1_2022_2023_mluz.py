def separarMultiplos(lista, k):
    resultado = []

    for n in lista:
        if (n % k == 0):
            resultado = resultado + [n]

    return resultado

print(separarMultiplos([1,2,3,4,5,6],2)) # Debería devolver [2,4,6]
print(separarMultiplos([4,15,16,21,32,33], 3)) # Debería devolver [15,21,33]

def notasEstudiantes(tabla):
    resultado = 0
    mayor = 0
    nombre_mayor = ""

    for fila in tabla:
        nombre = fila[0]
        nota = fila[2]
        resultado = resultado + nota
        if (nota > mayor):
            mayor = nota
            nombre_mayor = nombre

    resultado = resultado / len(tabla)

    return resultado, nombre_mayor

estudiantes = [
    ["Ane", 18, 5.5], 
    ["Gorka", 17, 9.8], 
    ["Iñaki", 17, 8.6], 
    ["Laura", 18, 3.5], 
    ["Jon", 18, 2.5]
]

print(notasEstudiantes(estudiantes)) # (5.98, “Gorka”)

def es_letra_numero(letra):
    resultado = True
    
    letra = letra.lower()

    if (letra in "0123456789abcdefghijklmnopqrstuvwxyz"):
        resultado = True
    else:
        resultado = False

    return resultado

def cambiarCadena(frase):
    resultado = ""

    vocales = "aeiouAEIOU"

    for letra in frase:
        if (letra in vocales):
            resultado = resultado + letra + letra
        elif (es_letra_numero(letra) == True):
            resultado = resultado + letra
        else:
            resultado = resultado + "_"

    return resultado

print(cambiarCadena("ae")) #aaee
print(cambiarCadena("¡Hola AMiGO! ¿Estás bien?")) #_Hoolaa_AAMiiGOO___EEst_s_biieen_

# Extra

def intercambiarMinMax(lista):
    resultado = []

    menor = lista[0]
    mayor = lista[0]

    for numero in lista:
        resultado = resultado + [numero]
        if (numero < menor):
            menor = numero
        if (numero > mayor):
            mayor = numero

    pos_menor = lista.index(menor)
    pos_mayor = lista.index(mayor)

    resultado[pos_menor] = mayor
    resultado[pos_mayor] = menor

    return resultado

lista = [1,2,6,54,10,-3]
print(intercambiarMinMax(lista)) #[1,2,6,-3,10,54]
