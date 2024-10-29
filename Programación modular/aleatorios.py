import random

tabla = []

for i in range(5):
    fila = []
    for j in range(5):
        fila.append(random.randint(1, 6))
    tabla.append(fila)

# print(tabla)

# Escribir tabla en fichero aleatorios.csv
fichero = open("aleatorios.csv", "w")

for fila in tabla:
    for elemento in fila:
        fichero.write(f"{str(elemento)};")
    fichero.write("\n")

fichero.close()

# Leer tabla desde fichero aleatorios.csv
tabla = []

fichero = open("aleatorios.csv", "r")

for linea in fichero:
    # procesar la línea del fichero
    campos = linea.split(";")
    fila = [campos[0], campos[1], campos[2], campos[3], campos[4]]
    tabla.append(fila)

fichero.close()

print(tabla)
