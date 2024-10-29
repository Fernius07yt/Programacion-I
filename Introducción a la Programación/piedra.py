import random

puntosHumana: int = 0
puntosMaquinas: int = 0

for i in range(5):
    # Las jugadas son 1: PIEDRA, 2: PAPEL, 3: TIJERAS
    print("Elige tu jugada:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    jugadaHumana: int = int(input("Opción: "))

    jugadaMaquinas: int = random.randint(1, 3)

    # Comprobar quién ha ganado
    # ¿Hemos empatado?
    if (jugadaHumana == jugadaMaquinas):
        pass
    # ¿Nos gana la máquina?
    elif ( (jugadaMaquinas == 1 and jugadaHumana == 3) or (jugadaMaquinas == 2 and jugadaHumana == 1) or (jugadaMaquinas == 3 and jugadaHumana == 2)):
        puntosMaquinas = puntosMaquinas + 1
    # Si no hemos empatado ni nos ha ganado la máquina, hemos ganado
    else:
        puntosHumana = puntosHumana + 1

    print(f"Puntos CPU: {puntosMaquinas}")
    print(f"Puntos raza humana: {puntosHumana}")