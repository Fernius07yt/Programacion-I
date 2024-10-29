# Entrada
altura:float = float(input("Altura: "))
anchura:float = float(input("Anchura: "))
ventanas:int = int(input("Ventanas: "))
puertas:int = int(input("Puertas: "))

# Procesamiento
area:float = altura * anchura - ventanas * 1 - puertas * 1.6
litros:float = area / 10

# Salida
print(f"Una pared de {altura} m de alto y {anchura} m de ancho con {ventanas} ventanas y {puertas} puerta necesita {litros} litros de pintura.")