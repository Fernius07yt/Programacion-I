def cargar_peliculas(peliculas):
    fichero = open("pelis.csv", "r", encoding="utf-8")

    for linea in fichero:
        campos = linea.split(";")
        titulo = campos[0]
        genero = campos[1]
        director = campos[2]
        pais = campos[3]
        pelicula = {"titulo": titulo, "genero": genero, "director": director, "pais": pais}
        peliculas.append(pelicula)

    fichero.close()

def mayor_participacion(peliculas):
    # Contar cuántas películas por genero
    contadores = {}

    for peli in peliculas:
        genero = peli["genero"]
        if (genero not in contadores):
            contadores[genero] = 1
        else:
            contadores[genero] = contadores[genero] + 1

    # Buscar el mayor valor en el diccionario de contadores
    """
    contadores = {
        "Drama": 3,
        "Romántica": 1,
        "Accion": 1
    }
    """

    mayor_clave = ""
    mayor_valor = 0

    for clave in contadores:
        valor = contadores[clave]
        if (valor > mayor_valor):
            mayor_clave = clave
            mayor_valor = valor

    return mayor_clave

def premioMasVotos(premios):
    mayor_clave = ""
    mayor_valor = 0

    for clave in premios:
        valor = premios[clave]
        if (valor["publico"] > mayor_valor):
            mayor_clave = clave
            mayor_valor = valor["publico"]
    
    print(f"El premio con mayor voto del público fue: {mayor_clave}")

    mayor_clave = ""
    mayor_valor = 0

    for clave in premios:
        valor = premios[clave]
        if (valor["jurado"] > mayor_valor):
            mayor_clave = clave
            mayor_valor = valor["jurado"]
    
    print(f"El premio con mayor voto del jurado fue: {mayor_clave}")

def guardar_peliculas(peliculas):
    fichero = open("pelis.csv", "w")

    for peli in peliculas:
        fichero.write(f"{peli['titulo']};{peli['genero']};{peli['director']};{peli['pais']};\n")

    fichero.close()

def guardar_premios(premios):
    fichero = open("premios.csv", "w")

    for clave in premios:
        valor = premios[clave]
        fichero.write(f"{clave};{valor['publico']};{valor['jurado']};\n")

    fichero.close()

peliculas = []

cargar_peliculas(peliculas)

print(peliculas)

premios = {
    "Concha de Oro": {"publico": 245, "jurado": 15},
    "Concha de Plata": {"publico": 168, "jurado": 17},
    "Premio Especial mejor direccion": {"publico": 355, "jurado": 11},
    "Premio Especial mejor interpretacion": {"publico": 360, "jurado": 13},
    "Premio Especial mejor guion": {"publico": 104, "jurado": 9}
}

guardar_premios(premios)