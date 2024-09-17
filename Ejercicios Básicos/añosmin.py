# Entrada del usuario para introducir sus años
años: int = int(input("¿Cuantos años tienes? "))

# Cálculo de los minutos que tienes
minutos: int = int(años) * 365 * 24 * 60

# Salida del número de minutos que tienes
print(f"Tienes {minutos} minutos")