# Solicita al usuario el numero de iteraciones para calcular Pi:
iteraciones = int(input("Ingrese el número de iteraciones para calcular PI: "))

# Calcula el valor aproximado de PI conforme al numero de iteraciones introducidas
for k in range(iteraciones):
    pi = ((-1) ** k) / ((2 * k) + 1)
    pi *= 4

# Muestra el resultado en pantalla
print(f"El valor aproximado de PI es: {pi}")