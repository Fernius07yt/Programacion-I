# Introducimos la constante de gravedad en m/s²
GRAVEDAD = 9.8

# Calculamos y mostramos la velocidad y el espacio recorrido durante un período de 10 segundos en un plano plano recto, con la gravedad de la Tierra.
for tiempo in range(0, 11):
    # Calculamos la velocidad y el espacio recorrido en este instante
    velocidad = GRAVEDAD * tiempo

    # Calculamos el espacio recorrido en este instante (distancia al suelo) en m
    espacio = 1/2 * GRAVEDAD * tiempo ** 2
    
    # Mostramos los resultados en pantalla para este instante
    print(f"t = {tiempo}, v = {velocidad:.1f} m/s, {espacio:.1f} m recorridos")