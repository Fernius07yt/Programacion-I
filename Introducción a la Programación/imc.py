# Entrada
peso:float = float(input("Peso (kg): "))
altura:float = float(input("Altura (m): "))

# Procesamiento
imc = peso / altura ** 2
valoracion: str = ""

if (imc < 18.5):
    valoracion = "Bajo peso"
elif (imc <= 25):
    valoracion = "Peso normal"
elif (imc <= 30):
    valoracion = "Sobrepeso"
else:
    valoracion = "Obesidad"

# Salida
print(f"IMC: {imc}")
print(valoracion)