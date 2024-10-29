frase:str = input("Frase: ")
contador:int = 0

for letra in frase:
    if (letra in "bcdfghjklmnpqrstvwxyz"):
        contador = contador + 1

print(f"Consonantes: {contador}")