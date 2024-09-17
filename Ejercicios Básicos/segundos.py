# Entrada de datos del usuario
segundos_1: int = int(input("Ingrese la cantidad de segundos: "))

# Calcula las horas, minutos y segundos correspondientes al número de segundos ingresados
horas: int = segundos_1 // 3600
minutos: int = (segundos_1 % 3600) // 60
segundos_2: int = segundos_1 % 60

# Imprime el resultado en horas, minutos y segundos
print(f"{segundos_1} segundos son {horas} horas, {minutos} minutos y {segundos_2} segundos.")