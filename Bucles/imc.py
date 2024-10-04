# Entrada de datos del usuario del peso y altura
peso: float = float(input("Introduce tu peso en kilogramos: "))
altura: float = float(input("Introduce tu altura en metros: "))

# Cálculo del índice de masa corporal (IMC)
imc: float = peso / (altura ** 2)

# Si el IMC es menor que 18.5, el usuario tiene bajo peso.
if (imc < 18.5):
    print(f"Tu IMC es {imc}. Tienes bajo peso.")

# Si el IMC es entre 18.5 y 25, el usuario tiene peso normal.
elif (18.5 <= imc < 25):
    print(f"Tu IMC es {imc}. Tienes peso normal.")

# Si el IMC es entre 25 y 30, el usuario tiene sobrepeso.
elif (25 <= imc < 30):
    print(f"Tu IMC es {imc}. Tienes sobrepeso.")

# Si el IMC es superior a 30, el usuario tiene obesidad.
else:
    print(f"Tu IMC es {imc}. Tienes obesidad.")