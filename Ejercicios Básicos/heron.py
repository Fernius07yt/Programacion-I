# Importamos la biblioteca matemática para calcular el área del triángulo
import math

# Pedimos al usuario que introduzca las longitudes de los lados del triángulo
a: float = float(input("Define la longitud del lado a: "))
b: float = float(input("Define la longitud del lado b: "))
c: float = float(input("Define la longitud del lado c: "))

# Calculamos el semiperímetro del triángulo
s = (a + b + c) / 2

# Calculamos el área del triángulo usando la fórmula de Herón
area = math.sqrt(s * (s - a) * (s - b) * (s - c))   

# Mostramos el área del triángulo en pantalla
print(f"Un triángulo con lados de {a}, {b} y {c} m tiene {area:.3f} m^2.")