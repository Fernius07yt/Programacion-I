def dosJuntoADos(lista):
    resultado = False
    anterior = 0

    for numero in lista:
        if (numero == 2 and anterior == 2):
            resultado = True
            break
        anterior = numero
    
    return resultado

print(dosJuntoADos([1, 2, 2, 4])) # True
print(dosJuntoADos([1, 2, 3, 4])) # False
print(dosJuntoADos([1, 2, 3, 2])) # False