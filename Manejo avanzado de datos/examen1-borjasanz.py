def contar_segundos(horas, minutos, segundos):
    resultado = horas * 3600 + minutos * 60 + segundos
    return resultado

#print(contar_segundos(1,20,30)) # Debería devolver 4830
#print(contar_segundos(0,0,15)) # Debería devolver 15

def separar_mayores(lista, numero):
    resultado = []

    for n in lista:
        if (n > numero):
            resultado.append(n)

    return resultado

#print(separar_mayores([1,2,3,4,5,6], 4)) # Debería devolver [5,6]
#print(separar_mayores([4,5,6,1,3], 3)) # Debería devolver [4,5,6]

def login(intentos):
    resultado = False

    for _ in range(intentos):
        user = input("User: ")
        password = input("Password: ")
        if (user == "user1" and password == "pass1"):
            resultado = True
            break

    return resultado

#print(login(5))

def ganador(lista):
    resultado = lista[0]

    for piloto in lista:
        tiempo_piloto = piloto[1]
        tiempo_resultado = resultado[1]

        if (contar_segundos(tiempo_piloto[0], tiempo_piloto[1], tiempo_piloto[2]) < contar_segundos(tiempo_resultado[0], tiempo_resultado[1], tiempo_resultado[2])):
            resultado = piloto

    return resultado

lista_pilotos = [["Piloto1",[1,20,10]], ["Piloto2",[1,25,13]], ["Piloto3",[1,19,18]]]

print(ganador(lista_pilotos))

