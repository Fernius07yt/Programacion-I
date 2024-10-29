#
# Entrada
nota:float = float(input("Nota (0-10): "))

# Procesamiento
calificacion:str = ""

if (nota < 5):
    calificacion = "Suspenso"
elif (nota < 7):
    calificacion = "Aprobado"
elif (nota < 9):
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"

# Salida
print(calificacion)