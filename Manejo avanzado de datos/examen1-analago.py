def obtenerLetraDNI(dni):
    resultado = ""

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    resto = int(dni) % 23

    resultado = letras[resto]

    return resultado

print(obtenerLetraDNI("12345678"))

def insertarLista(lista, numero):
    resultado = lista
    
    posicion = -1

    for pos, n in enumerate(lista):
        if (n == -1):
            posicion = pos
            resultado[posicion] = numero
            break

    if (posicion == -1):
        print("No se ha podido introducir el número en la lista")
 
    return resultado

print(insertarLista([1,-1,2,3,4,-1,5], 100))