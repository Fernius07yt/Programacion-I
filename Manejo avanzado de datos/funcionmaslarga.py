# Función que devuelve la palabra más larga de una frase
# recibe: frase (str)
# devuelve: la palabra más larga (str)
def mas_larga(frase):
    lista = frase.split(" ")

    resultado = lista[0]

    for palabra in lista:
        if (len(palabra) > len(resultado)):
            resultado = palabra

    return resultado

frase = input("Frase: ")
print(mas_larga(frase))