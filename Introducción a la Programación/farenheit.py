# Entrada
farenheit:float = float(input("Farenheit: "))

# Procesamiento
celsius:float = (farenheit - 32) / 1.8

# Salida
print(f"{farenheit} grados Farenheit son {celsius} grados Celsius")