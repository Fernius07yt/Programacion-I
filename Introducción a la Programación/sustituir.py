frase:str = input("Introduce una frase: ")
nueva:str = ""

for letra in frase:
    if (letra in "aeiouAEIOU"):
        nueva = nueva + "*"
    else:
        nueva = nueva + letra

print(nueva)