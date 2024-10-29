# Entrada
a:int = int(input("a: "))
b:int = int(input("b: "))
c:int = int(input("c: "))

# Procesamiento
menor:int = 0

# Con ifs anidados:
if (a <= b and a <= c):
    menor = a
else:
    if (b < c):
        menor = b
    else:
        menor = c

# Con elif
if (a <= b and a <= c):
    menor = a
elif (b <= a and b <= c):
    menor = b
elif (c <= a and c <= a):
    menor = c

# Salida
print(menor)