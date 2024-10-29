inicio:int = int(input("Inicio: "))
fin:int = int(input("Fin: "))
contador:int = 0

for i in range(fin, inicio-1, -1):
    if (i % 5 == 0):
        print(i)
        contador = contador + 1
        if (contador >= 3):
            break

contador = 0

for i in range(-fin, -inicio+1):
    if (i % 5 == 0):
        print(-i)
        contador = contador + 1
        if (contador >= 3):
            break

limite:int = fin - 3 * 5

for i in range(fin, limite, -1):
    if (i % 5 == 0):
        print(i)
