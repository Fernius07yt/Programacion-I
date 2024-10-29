frase:str = input("Introduce una frase: ")
contador:int = 0

for letra in frase:
    if (letra == " "):
        contador = contador + 1

print(f"{contador} espacios")