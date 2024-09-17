# Solicitar la temperatura en grados Fahrenheit al usuario
temp_f: float = float(input("Ingrese la temperatura en grados Fahrenheit: "))

# Convertir grados Fahrenheit a grados Celsius
temp_c: float = (temp_f - 32) / 1.8

# Mostrar la temperatura en grados Celsius al usuario
print(f"{temp_f} grados Fahrenheit equivalen a {temp_c} grados Celsius.")