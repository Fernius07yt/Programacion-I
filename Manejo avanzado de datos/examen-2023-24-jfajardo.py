libros = [["001", "Cien annos de soledad", "Gabriel Garcia Marquez", 1982, 6],
          ["002", "El señor de los anillos", "Gabriel Garcia Marquez", 1954, 12],
          ["003", "Un mundo feliz", "Aldous Huxley", 1932, 3],
          ["004", "Orgullo y prejuicio", "Jane Austen", 1813, 1],
          ["005", "Crimen y castigo", "Fiodor Dostoyevski", 1866, 2],
          ["006", "Lolita", " Vladimir Nabokov", 1955, 8],
          ["007", "Ulises", "James Joyce", 1920, 4],
          ["008", "Madame Bovary", "Gustave Flaubert", 1857, 1],
          ["009", "En busca del tiempo perdido", "Marcel Proust", 1914, 3],
          ]

prestamos = [["006", "Ana B. Lago", 20],
             ["008", "Lidia Rodriguez", 15],
             ["005", "Borja Sanz", 31],
             ["002", "Mari Luz Guenaga", 31],
             ["003", "Pablo Garairzar", 20],
             ["005", "Xabier Cantero", 15],
             ["001", "Mikel Emaldi", 15],
             ["002", "Leire Gomez", 31],
             ["002", "Carmen Sanchez", 15],
             ["009", "Pedro Garcia", 31]
             ]

libros = [{"codigo": "001", "titulo": "Cien annos de soledad", "autoria": "Gabriel Garcia Marquez", "año": 1982, "ejemplares": 6},
          {"codigo": "002", "titulo": "El señor de los anillos", "autoria": "Gabriel Garcia Marquez", "año": 1954, "ejemplares": 12},
          {"codigo": "003", "titulo": "Un mundo feliz", "autoria": "Aldous Huxley", "año": 1932, "ejemplares": 3},
          {"codigo": "004", "titulo": "Orgullo y prejuicio", "autoria": "Jane Austen", "año": 1813, "ejemplares": 1},
          {"codigo": "005", "titulo": "Crimen y castigo", "autoria": "Fiodor Dostoyevski", "año": 1866, "ejemplares": 2},
          {"codigo": "006", "titulo": "Lolita", "autoria": "Vladimir Nabokov", "año": 1955, "ejemplares": 8},
          {"codigo": "007", "titulo": "Ulises", "autoria": "James Joyce", "año": 1920, "ejemplares": 4},
          {"codigo": "008", "titulo": "Madame Bovary", "autoria": "Gustave Flaubert", "año": 1857, "ejemplares": 1},
          {"codigo": "009", "titulo": "En busca del tiempo perdido", "autoria": "Marcel Proust", "año": 1914, "ejemplares": 3},
          ]

prestamos = [{"codigo": "006", "cliente": "Ana B. Lago", "dias": 20},
             {"codigo": "008", "cliente": "Lidia Rodriguez", "dias": 15},
             {"codigo": "005", "cliente": "Borja Sanz", "dias": 31},
             {"codigo": "002", "cliente": "Mari Luz Guenaga", "dias": 31},
             {"codigo": "003", "cliente": "Pablo Garairzar", "dias": 20},
             {"codigo": "005", "cliente": "Xabier Cantero", "dias": 15},
             {"codigo": "001", "cliente": "Mikel Emaldi", "dias": 15},
             {"codigo": "002", "cliente": "Leire Gomez", "dias": 31},
             {"codigo": "002", "cliente": "Carmen Sanchez", "dias": 15},
             {"codigo": "009", "cliente": "Pedro Garcia", "dias": 31}
             ]


# Ejercicio 1

def prestamoActivoLibro (codigo, prestamos):
    resultado = False

    for p in prestamos:
        if (p["codigo"] == codigo):
            resultado = True
            break

    return resultado

print(prestamoActivoLibro("004", prestamos))

# Ejercicio 2

def libroMasEjemplares (libros):
    resultado = libros[0]

    for libro in libros:
        if (libro["ejemplares"] > resultado["ejemplares"]):
            resultado = libro

    return resultado

def libroMasTitulo (libros):
    resultado = libros[0]

    for libro in libros:
        if (len(libro["titulo"]) > len(resultado["titulo"])):
            resultado = libro

    return resultado



# Ejercicio 3
def cuantasVecesPrestado (codigo, prestamos):
    resultado = 0

    for p in prestamos:

        
        if (p["codigo"] == codigo):
            resultado = resultado + 1

    return resultado


def disponibilidadActualLibros(libros, prestamos):
    resultado = []

    for libro in libros:
        codigo = libro["codigo"]
        resultado.append([ libro["titulo"], libro["ejemplares"] - cuantasVecesPrestado(codigo, prestamos)])

    return resultado

print(disponibilidadActualLibros(libros, prestamos))

# Ejercicio 4

def promedioDias(prestamos):
    resultado = 0

    for p in prestamos:
        resultado = resultado + p[2]

    resultado = resultado / len(prestamos)

    return resultado

# Ejercicio opcional
def ultimask(palabra, k):
    resultado = ""

    if (len(palabra) < k):
        resultado = -1
    else:
        reves = ""
        for letra in palabra:
            reves = letra + reves
        resultado = reves[0:k]

    return resultado

def cadenas (palabras, k):
    resultado = []

    for palabra in palabras:
        resultado.append(ultimask(palabra, k))

    return resultado


print(libros[0].values())