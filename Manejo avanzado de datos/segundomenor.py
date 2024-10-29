# Función que devuelve el segundo menor número de una lista de números
# recibe: la lista de números
# devuelve: el 2o menor de esos números
def segundo_menor(lista):
    resultado = min(lista)
    lista.remove(resultado)
    resultado = min(lista)
    return resultado

def segundo_menor(lista):
    lista.sort()
    resultado = lista[1]
    return resultado

lista = [34.7, 12.6, 11.9, 23.4, 45.7, 5.3, 7.2, 3.1]

print(segundo_menor(lista))