import math

# Entrada
a:float = float(input("a: "))
b:float = float(input("b: "))
c:float = float(input("c: "))

# Procesamiento
s:float = (a + b + c) / 2
area:float = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Salida
print(f"Un triángulo con lados de {a}, {b} y {c} m tiene {area} m2")