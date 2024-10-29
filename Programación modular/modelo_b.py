def cargar_datos():
    resultado = {}

    fichero = open("peliculas.csv", "r", encoding="utf-8")

    for linea in fichero:
        # Origen;7.3;23424
        # resultado["Origen"] = { "nota": 7.3, "revisiones": 23424 }
        campos = linea.split(";")
        titulo = campos[0]
        nota = float(campos[1])
        revisiones = int(campos[2])
        resultado[titulo] = { "nota": nota, "revisiones": revisiones}

    fichero.close()

    return resultado