import random

secreto:int = random.randint(1, 100)

intentos:int = 5

acertado:bool = False

while (intentos > 0 and acertado == False):
    print(f"Intentos: {intentos}")
    intento:int = int(input("Introduce un número: "))
    if (intento == secreto):
        acertado = True
    else:
        if (secreto > intento):
            print("El número secreto es mayor")
        else: 
            print("El número secreto es menor")
    intentos = intentos - 1
    
if (acertado == True):
    print("¡Has acertado!")
else:
    print("Lo siento, has perdido.")