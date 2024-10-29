def morse(frase):
    resultado = ""

    frase = frase.upper()

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    simbolos = [".-", "-...", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-.", "-.-."]

    for letra in frase:
        posicion = alfabeto.index(letra)
        resultado = resultado + simbolos[posicion]

    return resultado