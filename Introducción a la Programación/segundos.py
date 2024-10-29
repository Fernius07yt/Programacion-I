# Entrada
iniciales:int = int(input("Segundos: "))

# Procesamiento
horas:int = iniciales // 3600
resto:int = iniciales % 3600
minutos:int = resto // 60
segundos:int = resto % 60

# Salida
print(f"{iniciales} segundos son {horas} horas, {minutos} minutos y {segundos} segundos.")