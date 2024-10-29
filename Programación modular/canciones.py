import random

canciones = []


# Leemos las canciones del fichero de canciones.csv
fichero = open("canciones.csv", "r")

for linea in fichero:
    campos = linea.split(";")
    artista = campos[0]
    titulo = campos[1]
    duracion = int(campos[2])
    cancion = {"artista": artista, "titulo": titulo, "duracion": duracion }
    canciones.append(cancion)

fichero.close()

# Creamos 10000 canciones nuevas
for i in range(10000):
    cancion = {
        "artista": "artista" + str(i), 
        "titulo": "titulo" + str(i), 
        "duracion": random.randint(100, 200) 
        }
    canciones.append(cancion)

print(canciones)

# Guardamos las canciones en el fichero canciones.csv
fichero = open("canciones.csv", "w")

for cancion in canciones:
    fichero.write(f'{cancion["artista"]};{cancion["titulo"]};{cancion["duracion"]};\n')

fichero.close()

