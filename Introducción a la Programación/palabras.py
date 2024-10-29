# palabras.py: Recibimos una frase y nos dice cuántas palabras tiene esa frase
frase:str = input("Introduce una frase: ")
contador:int = 1

for letra in frase:
    if (letra == " "):
        contador = contador + 1

print(f"{contador} palabras")