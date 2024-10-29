# Entrada
n:int = int(input("Número: "))

# Procesamiento
resultado = 0

for i in range(0, n+1):
    resultado = resultado + i

# Salida
print(f"Sumatorio de 0 a {n} = {resultado}")