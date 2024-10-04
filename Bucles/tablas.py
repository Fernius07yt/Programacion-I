# Repetimos sobre los números del 1 al 10
for i in range(1, 11):
    # Para cada número 'i', repetimos nuevamente del 1 al 10
    for j in range(1, 11):
        # Imprimimos el resultado de la multiplicación de 'i' y 'j', es decir, las tablas de multiplicación del numero 1 al 10.
        print(f"{i} x {j} = {i * j}")