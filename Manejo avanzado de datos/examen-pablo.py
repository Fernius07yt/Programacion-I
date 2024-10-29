def precio(frase):
    resultado = 5.0

    frase = frase.lower()

    for letra in frase:
        if (letra in "aeiou"):
            resultado = resultado + 0.5
        elif (letra in "0123456789"):
            resultado = resultado + 0.75
        else:
            resultado = resultado + 1

    return resultado


print(precio("hola"))


def masCaro(lista):
    resultado = lista[0]

    for frase in lista:
        if (precio(frase) > precio(resultado)):
            resultado = frase

    return resultado

