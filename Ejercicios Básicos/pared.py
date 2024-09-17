# Solicitar los datos de la pared al usuario
altura: float = float(input("Ingrese la altura de la pared: "))
anchura: float = float(input("Ingrese la anchura de la pared: "))
ventanas: int = int(input("Cuantas ventanas tiene la pared: "))
puertas: int = int(input("Cuantas puertas tiene la pared: "))

# Definir las dimensiones de las ventanas y puertas en metros cuadrados
dimension_ventana: float = 1 
dimension_puertas: float = 1.6

# Cálculo de la pintura necesaria en litros (1 litro = 10 m^2)
pintura_necesaria: float = (altura * anchura - (ventanas * dimension_ventana + puertas * dimension_puertas)) / 10

# Salida de la pintura necesaria en litros
print(f"Una pared de {altura} m de alto y {anchura} m de ancho con {ventanas} ventanas y {puertas} puerta necesita {pintura_necesaria:.2f} litros de pintura.")
