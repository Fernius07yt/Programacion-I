def antes(a:str, b:str) -> str:
    resultado:str = ""
    if (a.upper() < b.upper()):
        resultado = a
    else:
        resultado = b
    return resultado

# Programa principal
palabra1 = input("primera palabra? ")
palabra2 = input("segunda palabra? ")

print(f"{antes(palabra1, palabra2)} va antes en el diccionario")

