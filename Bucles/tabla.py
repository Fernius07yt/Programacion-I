# Pide al usuario que introduzca un número entero.
numero: int = int(input("Introduce un número entero: "))

# Si el número introducido es negativo, muestra un mensaje de error y pide que introduzca un número entero positivo. 
while numero < 0:
    print("Error: Introduce un número entero positivo.")
    numero: int = int(input("Introduce un número entero: "))

# Repite la multiplicación del número por cada número del 1 al 10 y lo muestra en pantalla. Muestra toda la tabla de multiplicación del número introducido.
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}") 