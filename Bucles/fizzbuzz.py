# Se realiza un bucle del 1 al 100
for i in range(1, 101):
    # Si el número es divisible por 3 y 5, imprime "FizzBuzz"
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")

    # Si el número es divisible por 3, imprime "Fizz"
    elif (i % 3 == 0):
        print("Fizz")

    # Si el número es divisible por 5, imprime "Buzz"
    elif (i % 5 == 0):
        print("Buzz")

    # Si el número no cumple ninguna de las condiciones anteriores, imprime el número en sí
    else:
        print(i)