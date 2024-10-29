# ultima.py: Recibe una frase y muestra solo la última palabra
def reves(frase: str) -> str:
    resultado:str = ""
    for letra in frase:
        resultado = letra + resultado
    return resultado

def primera(frase: str) -> str:
    resultado:str = ""
    for letra in frase:
        if (letra == " "):
            break
        resultado = resultado + letra
    return resultado

frase:str = input("Introduce una frase: ")

frase = reves(frase)
frase = primera(frase)
frase = reves(frase)

print(frase)


