def dos_y_cuatro(lista):
    resultado = True

    hay2 = 2 in lista
    hay4 = 4 in lista
    
    if (hay2 or hay4 and not (hay2 and hay4)):
        resultado = True
    else:
        resultado = False

    return resultado

print(dos_y_cuatro([1, 2, 3]))
print(dos_y_cuatro([3, 4, 5]))
print(dos_y_cuatro([1, 3, 5]))
print(dos_y_cuatro([1, 2, 3, 4]))

lista = []

for _ in range(5):
    numero = int(input("Introduce un número: "))
    lista.append(numero)

print(dos_y_cuatro(lista))