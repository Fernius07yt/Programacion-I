# Solicita al usuario 2 numeros de incio y fin
num_1: int = int(input("Introduce un numero de inicio: "))
num_2: int = int(input("Introduce un numero de fin: "))

# Inicia un contador en 0 para saber cuántos números pares ha impreso
contador = 0

# Imprime los números pares en el rango dado, hasta que se imprimen 5 números.
for i in range(num_1, num_2 + 1):

    # Si el número es par, imprimelo y incrementa el contador.
    if i % 2 == 0:
        print(i)
        contador += 1
    
    # Si se ha impreso 5 números pares, detiene el bucle.
    elif contador == 5: 
        break