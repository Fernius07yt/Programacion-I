def filtrar_canciones(canciones, artista):
    resultado = []

    for cancion in canciones:
        if (cancion["artista"] != artista):
            resultado.append(cancion)

    return resultado

canciones = [
    {"artista": "Anuel AA", "titulo": "Amanece"},
    {"artista": "Anuel AA", "titulo": "Ayuer"},
    {"artista": "Rosalía", "titulo": "Despechá"},
    {"artista": "Anuel AA", "titulo": "Brindemos"},
    {"artista": "Kiko Rivera", "titulo": "El mambo"},
]

print(filtrar_canciones(canciones, "Anuel AA"))

# Contar cuántas canciones tiene cada artista:
# preparamos un diccionario de contadores donde la clave es el artista y el valor el contador
contadores = {}

for cancion in canciones:
    artista = cancion["artista"]
    if (artista not in contadores):
        contadores[artista] = 1
    else:
        contadores[artista] = contadores[artista] + 1

print(contadores)

# Agrupar títulos de caciones por artista:
# preparamos un diccionario donde la clave es el artista y el valor una lista de títulos
titulos_por_artista = {}

for cancion in canciones:
    artista = cancion["artista"]
    titulo = cancion["titulo"]
    if (artista not in titulos_por_artista):
        titulos_por_artista[artista] = [ titulo ]
    else:
        titulos_por_artista[artista] = titulos_por_artista[artista] + [ titulo ]

print(titulos_por_artista)

# Buscar el artista con más canciones en este diccionario:

titulos_por_artista = {
    'Anuel AA': ['Amanece', 'Ayuer', 'Brindemos'], 
    'Rosalía': ['Despechá'], 
    'Kiko Rivera': ['El mambo']
}

mayor_clave = ""
mayor_valor = 0

for clave in titulos_por_artista:
    valor = titulos_por_artista[clave]
    if (len(valor) > mayor_valor):
        mayor_clave = clave
        mayor_valor = len(valor)

print(f"El artista con más canciones es {mayor_clave}")