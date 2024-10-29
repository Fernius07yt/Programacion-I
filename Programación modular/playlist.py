cancion1 = { "titulo": "cancion 1", "artista": "artista 1", "duracion": 147.5 }
cancion2 = { "titulo": "cancion 2", "artista": "artista 1", "duracion": 117.5 }
cancion3 = { "titulo": "cancion 3", "artista": "artista 2", "duracion": 271.5 }

playlist = [cancion1, cancion2, cancion3]

print(cancion1["duracion"])
print(cancion1)
print(playlist)

def duracion_total(playlist):
    resultado = 0

    for cancion in playlist:
        resultado = resultado + cancion["duracion"]

    return resultado

def cancion_mas_larga (playlist):
    resultado = playlist[0]

    for cancion in playlist:
        if (cancion["duracion"] > resultado["duracion"]):
            resultado = cancion

    return resultado

mas_larga = cancion_mas_larga(playlist)

print(mas_larga["titulo"])
