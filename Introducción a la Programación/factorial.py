# Entrada
n:int = int(input("Número: "))

# Procesamiento
resultado = 1
for i in range(1, n+1):
    resultado = resultado * i

# Salida
print(f"{n}! = {resultado}")
