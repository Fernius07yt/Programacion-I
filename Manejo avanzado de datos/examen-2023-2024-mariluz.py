# Ejercicio 1
def ultimaContiene(lista, k):
    resultado = ""

    for palabra in lista:
        if (len(palabra) >= k):
            resultado = palabra
 
    return resultado

lista = ["perro", "gato", "ratón", "elefante", "avestruz", "sardina", "rata", "atún"]
print(ultimaContiene(lista, 5)) #Debe mostrar sardina
print(ultimaContiene(lista, 8)) #Debe mostrar avestruz

# Ejercicio 2
def multiplos (lista, k):
    resultado = []

    for n in lista:
        if (n % k == 0):
            resultado.append(n)

    return resultado

# Ejercicio 3
def mover_jugador(frase):
    x = 0
    y = 0
    monedas = 0

    for letra in frase:
        if (letra in "aeiouAEIOU"):
            x = x + 1
        elif (letra in "0123456789"):
            x = x - 1
        elif (letra in "bcdfghjklmnpqrstvwxyz"):
            y = y + 1
        elif (letra in "BCDFGHJKLMNPQRSTVWXYZ"):
            y = y - 1
        else:
            monedas = monedas + 1

    return (x, y, monedas)

print(mover_jugador("a"))