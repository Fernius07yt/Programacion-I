numero:int = int(input("Numero: "))

resultado:float = 0

for i in range(0, numero+1):
    resultado = resultado + ((-1)**i / (2*i + 1))

resultado = resultado * 4

print(f"PI = {resultado}")