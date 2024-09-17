# Importamos las bibliotecas necesarias
import math

# Petición de datos del usuario
velocidad: float = float(input("Ingrese la velocidad inicial (en m/s): "))
angulo_salto: float = float(input("Ingrese el ángulo de salto (en grados): "))
gravedad: float = float(input("Ingrese la aceleración de la gravedad (en m/s²): "))

# Conversión del ángulo de salto a radianes. La función math.radians convierte grados a radianes.
angulo_rad = math.radians(angulo_salto)

# Cálculo de la longitud recorrida durante el salto. La fórmula para la velocidad y el ángulo de salto es: v² * sin(2θ) / g
longitud = (velocidad ** 2 * math.sin(2 * angulo_rad)) / gravedad

# Salida de la longitud recorrida durante el salto en metros. Usamos 3 decimales para la precisión.
print(f"Una persona que salte con un ángulo de {angulo_salto}º a {velocidad} m/s en un planeta con g = {gravedad} m/s2 recorrería {longitud:.3f} m.")