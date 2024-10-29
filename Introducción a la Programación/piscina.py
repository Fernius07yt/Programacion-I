# Entrada
ancho:float = float(input("Ancho: "))
largo:float = float(input("Largo: "))
profundidad:float = float(input("Profundidad: "))

# Procesamiento
volumen:float = ancho * largo * profundidad
litros:float = volumen * 1000

# Salida
print(f"Una piscina de {largo} m de largo, {ancho} m de ancho y {profundidad} m de profundidad contiene {litros} litros de agua.")
