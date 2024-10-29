frase:str = input("Introduce una frase: ")
nueva:str = ""

for letra in frase:
    nueva = letra + nueva

print(nueva)