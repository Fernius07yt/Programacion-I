# bucle for: cuando sabemos cuántas vueltas tiene que dar
for i in range(100):
    print("Hola")


# bucle while: cuando no sabemos cuántas vueltas tiene que dar
i = 100
while (i > 0):
    print("Hola")
    i = i - 1

respuesta = input("¿Quieres jugar? (s/n) ")
while (respuesta == "s"):
    print("Jugar")
    respuesta = input("¿Quieres jugar? (s/n) ")
    