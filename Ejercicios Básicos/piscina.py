# Entrada de datos del usuario para calcular el volumen
ancho: float = float(input("Ingrese el ancho de la piscina: "))
largo: float = float(input("Ingrese el largo de la piscina: "))
profundidad: float = float(input("Ingrese la profundidad de la piscina: "))

# Cálculo del volumen de la piscina
volumen_piscina: float = ancho * largo * profundidad

# Conversion del volumen de la piscina a litros (1m^3 = 1000 L)
litros_agua: float = volumen_piscina * 1000

# Salida del volumen de la piscina en litros
print(f"Una piscina de {largo} m de largo, {ancho} m de ancho y {profundidad} m de profundidad contiene {litros_agua} litros de agua.")