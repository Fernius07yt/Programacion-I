import math

# Entrada
a:float = float(input("a: "))
b:float = float(input("b: "))
c:float = float(input("c: "))

# Procesamiento
x1 = (-b + math.sqrt(b**2 - 4 * a * c ) ) / 2 * a
x2 = (-b - math.sqrt(b**2 - 4 * a * c ) ) / 2 * a

# Salida
print(f"Raices de {a} x2 + {b} x + {c} = 0:")
print(f"x = {x1}")
print(f"x = {x2}")