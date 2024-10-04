# Se solicita al usuario que introduzca un número de inicio y de fin, y se convierte a entero
num_1: int = int(input("Introduce un numero de inicio: "))
num_2: int = int(input("Introduce un numero de fin: "))

# Inicializa un contador en cero para llevar la cuenta de los múltiplos de 5 encontrados
contador = 0

# Se itera desde num_2 hasta num_1, decrementando en 1 en cada iteración
for i in range(num_2, num_1-1, -1):
    
    # Se verifica si el número actual es múltiplo de 5, se muestra al usuario y se incrementa en 1 el valor del contador
    if i % 5 == 0:
        print(i)
        contador = contador + 1
    
        # Se verifica si se han encontrado 3 múltiplos de 5 y si es verdadero, se interrumpe
        if contador == 3: 
            break