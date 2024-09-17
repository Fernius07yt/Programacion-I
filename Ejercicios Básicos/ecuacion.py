# Importamos la biblioteca matemática para calcular las raices
import math

# Solicitamos los valores de a, b y c al usuario para la ecuación de segundo grado
print("Este programa calcula las raizes de una ecuacion de segundo grado. ax^2 + bx + c = 0")
a: int = int(input("Introduce el valor de a: "))
b: int = int(input("Introduce el valor de b: "))
c: int = int(input("Introduce el valor de c: "))

# Calculamos las raices utilizando la fórmula de ecuaciones de segundo grado
x1: float = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2: float = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

# Mostramos las raices en pantalla
print(f"Raices de {a}x^2 + {b}x + {c} = 0 son x = {x1} y x = {x2}")