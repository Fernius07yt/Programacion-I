import math

# Entrada
velocidad:float = float(input("velocidad: "))
angulo:float = float(input("angulo en grados: "))
g:float = float(input("g: "))

# Procesamiento
radianes:float = math.radians(angulo)
longitud:float = (velocidad**2 * math.sin(2 * radianes)) / g

# Salida
print(f"Una persona que salte con un ángulo de {angulo}º a {velocidad} m/s en un planeta con g = {g} m/s2 recorrería {longitud} m.")