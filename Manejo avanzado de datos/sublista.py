# Función que indica si la lista b es una sublista de la lista a
# recibe: a (list), b (list)
# devuelve: True/False
def sublista(a, b):
    resultado = True

    for elemento in b:
        if (elemento not in a):
            resultado = False
            break

    return resultado

print(sublista([1,2,3,4,5], [1,2,3])) # True
print(sublista([1,2,3,4,5], [1,2,5])) # True
print(sublista([1,2,3,4,5], [7,2,5])) # False
