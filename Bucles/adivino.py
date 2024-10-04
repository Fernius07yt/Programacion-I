# Importa el módulo random para generar números aleatorios
import random

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicia un bucle que permite al usuario hacer hasta 5 intentos
for intento in range(1, 6):
    numero_usuario = int(input(f"Intento {intento}: Adivina el número: "))

    # Si el número introducido coincide con el generado aleatoriamente, muestra un mensaje de éxito y termina el bucle
    if numero_usuario == numero_secreto:
        print("Has acertado!")
        break
    
    # Si el número introducido es menor o mayor que el generado, muestra un mensaje de aviso
    elif numero_usuario < numero_secreto:
        print("El número que estoy pensando es mayor")
    else:  
        print("El número que estoy pensando es menor")

# Muestra el número si no se adivina en 5 intentos
else:  
    print(f"El número que estaba pensando era {numero_secreto}")