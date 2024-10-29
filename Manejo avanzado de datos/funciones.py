# Funcion mayor: devuelve el mayor de dos números
# recibe a (numero), b (numero)
# devuelve el numero mayor entre a y b
def mayor (a, b):
    resultado = 0
    if (a > b):
        resultado = a
    else:
        resultado = b
    return resultado

a = int(input("A:"))
b = int(input("B:"))

n = mayor(a, b)

print(n)

#############################################

a = 3
b = 7
resultado = 0
if (a > b):
    resultado = a
else:
    resultado = b
    
print(resultado)