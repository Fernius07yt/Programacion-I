# Pide al usuario que introduzca un número entero
numero: int = int(input("Introduce un número entero: "))

# Inicializa el factorial a 1 para que el producto sea calculado correctamente.
factorial: int = 1

# Calcula el factorial del número introducido y lo muestra en pantalla.
for i in range(1, numero + 1):
    factorial *= i
    print(f"El factorial de {numero} es {factorial}")