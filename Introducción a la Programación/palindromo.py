def reves(palabra:str) -> str:
    resultado:str = ""
    for letra in palabra:
        resultado = letra + resultado
    return resultado

def es_palindromo(palabra:str) -> bool:
    resultado:bool = False
    if (palabra == reves(palabra)):
        resultado = True
    return resultado

def es_palindromo_indices(palabra:str) -> bool:
    resultado:bool = True
    for i in range(len(palabra)):
        j = len(palabra) - 1 - i
        if (palabra[i] != palabra[j]):
            resultado = False
            break
    return resultado

print(es_palindromo("radar")) # True
print(es_palindromo("rodar")) # False
print(es_palindromo_indices("radar")) # True
print(es_palindromo_indices("rodar")) # False