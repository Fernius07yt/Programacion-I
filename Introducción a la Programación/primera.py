# primera.py: Recibe una frase y muestra solo la primera palabra
frase:str = input("Introduce una frase: ")
primera:str = ""

for letra in frase:
    if (letra == " "):
        break
    primera = primera + letra

print(primera)