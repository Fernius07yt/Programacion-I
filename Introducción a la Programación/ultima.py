# ultima.py: Recibe una frase y muestra solo la última palabra
frase:str = input("Introduce una frase: ")
ultima:str = ""

for letra in frase:
    if (letra == " "):
        ultima = ""
    else:
        ultima = ultima + letra

print(frase)


