# Pide al usuario que introduzca un número entero.
num: int = int(input("Introduce un número entero: "))

# Introduce al valor suma el valor 0
suma = 0

# Repite desde 1 hasta el número introducido (inclusive) y suma cada número
for i in range(1, num + 1):
    suma += i

# Muestra el resultado de la suma
print(f"La suma de los primeros {num} números es: {suma}")