def cargar_datos(peliculas):
    fichero = open("peliculas.csv", "r", encoding="utf8")

    for linea in fichero:
        campos = linea.split(";")
        titulo = campos[0]
        nota = float(campos[1])
        revisiones = int(campos[2])
        pelicula = [ titulo, nota, revisiones ]
        peliculas.append(pelicula)

    fichero.close()

def obtener_nota(peliculas, titulo):
    resultado = 0.0

    for peli in peliculas:
        t = peli[0]
        nota = peli[1]
        if (t == titulo):
            resultado = nota
            break

    return resultado

def nota_media_reviews(peliculas, minimo):
    resultado = 0
    contador = 0

    for peli in peliculas:
        nota = peli[1]
        revisiones = peli[2]
        if (revisiones >= minimo):
            resultado = resultado + nota
            contador = contador + 1

    resultado = resultado / contador

    return resultado

def nota_media(peliculas):
    resultado = 0

    for peli in peliculas:
        nota = peli[1]
        resultado = resultado + nota

    resultado = resultado / len(peliculas)

    return resultado

def mas_reviews(peliculas):
    resultado = peliculas[0]

    for peli in peliculas:
        if (peli[2] > resultado[2]):
            resultado = peli

    return resultado


peliculas = []
cargar_datos(peliculas)
print(len(peliculas)) # Devuelve 824778
print(peliculas[0])
print(nota_media(peliculas))
print(obtener_nota(peliculas, "War Games")) # Devuelve 8.8 
print(nota_media_reviews(peliculas, 600)) # Devuelve 7.06