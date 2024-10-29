def cesar(frase:str, clave:int) -> str:
    resultado:str = ""
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letra in frase:
        # Ponemos la letra en mayúsculas
        letra = letra.upper()
        # Miramos si la letra se puede cifrar
        if (letra in alfabeto):
            # Buscamos la posición de la letra en el alfabeto
            posicion:int = alfabeto.index(letra)
            posicion = posicion + clave
            if (posicion >= len(alfabeto)):
                posicion = posicion - len(alfabeto)
            resultado = resultado + alfabeto[posicion]
        else:
            # Si no se puede cifrar, la copiamos tal cual
            resultado = resultado + letra
    return resultado

def descesar(frase:str, clave:int) -> str:
    return cesar(frase, -clave)    

def vigenere(frase:str, clave:list) -> str:
    resultado:str = ""
    posicion:int = 0
    for letra in frase:
        # Ciframos la letra con la clave que toque
        resultado = resultado + cesar(letra, clave[posicion])
        # Pasamos a la siguiente clave de la lista
        posicion = posicion + 1
        # Si nos hemos pasado de posición, volvemos a cero
        if (posicion >= len(clave)):
            posicion = 0
    return resultado

def desvigenere(frase:str, clave:list) -> str:
    resultado:str = ""
    posicion:int = 0
    for letra in frase:
        # Ciframos la letra con la clave que toque
        resultado = resultado + cesar(letra, -clave[posicion])
        # Pasamos a la siguiente clave de la lista
        posicion = posicion + 1
        # Si nos hemos pasado de posición, volvemos a cero
        if (posicion >= len(clave)):
            posicion = 0
    return resultado

print(cesar("HOLA", 3)) # KROD
print(descesar("KROD", 3)) # HOLA
print(vigenere("HOLA", [3,3,3,3])) # KROD
print(vigenere("HOLA", [3,2,1,4])) # KQME
print(desvigenere("KQME", [3,2,1,4])) # HOLA

