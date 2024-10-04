# Mostramos al usuario las opciones disponibles de la calculadora
print("Opciones: \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir")

# Solicitamos al usuario que elija una opción y almacenamos su respuesta
operacion = int(input("¿Qué operación deseas realizar? (1, 2, 3, 4) "))

# Validamos que la opción sea correcta y mostramos un mensaje de error si es incorrecta
while operacion < 1 or operacion > 4:
    print("Opción incorrecta. Vuelve a intentarlo.")
    operacion = int(input("¿Qué operación deseas realizar? (1, 2, 3, 4) "))

# Si se elige la opción 1, se pide 2 numeros, se realiza la operacion de suma con los numeros seleccionados y se muestra el resultado
if operacion == 1:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es: {resultado}")

# Si se elige la opción 2, se pide 2 numeros, se realiza la operacion de resta con los numeros seleccionados y se muestra el resultado
elif operacion == 2:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} es: {resultado}")

# Si se elige la opción 3, se pide 2 numeros, se realiza la operacion de multiplicación con los numeros seleccionados y se muestra el resultado
elif operacion == 3:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} es: {resultado}")

# Si se elige la opción 4, se pide 2 numeros, se realiza la operacion de división con los numeros seleccionados y se muestra el resultado
elif operacion == 4:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    # Validamos que el segundo número no sea cero y mostramos un mensaje de error si es así. Si no, se calcula sin problemas
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    else:
        print("No se puede dividir por cero.")

