# Importamos la libreria random
import random

# Mostramos las opciones de jugadas posibles
print("Jugadas: \n 1. Piedra \n 2. Papel \n 3. Tijera")

# El usuario elige una jugada
jugada_usuario = int(input("¿Qué jugada escogerá? "))

# La maquina de manera aleatoria elige una jugada
jugada_maquina = random.randint(1, 3)

# Si el usuario ha elegido la opcion 1 (Piedra), compara con la opcion de la maquina y muestra un resultado
if jugada_usuario == 1:
    if jugada_maquina == 1:
        print("Empate!")
    elif jugada_maquina == 2:
        print("Perdiste! La maquina escogió papel.")
    else:
        print("Ganaste! La maquina escogió tijera.")

# Si el usuario ha elegido la opcion 2 (Papel), compara con la opcion de la maquina y muestra un resultado
elif jugada_usuario == 2:
    if jugada_maquina == 1:
        print("Ganaste! La maquina escogió piedra.")
    elif jugada_maquina == 2:
        print("Empate!")
    else:
        print("Perdiste! La maquina escogió tijera.")

# Si el usuario ha elegido la opcion 3 (Tijera), compara con la opcion de la maquina y muestra un resultado
elif jugada_usuario == 3:
    if jugada_maquina == 1:
        print("Perdiste! La maquina escogió piedra.")
    elif jugada_maquina == 2:
        print("Ganaste! La maquina escogió papel.")
    else:
        print("Empate!")