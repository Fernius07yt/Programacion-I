import random

def cargar_libros(libros):
    fichero = open("libros.csv", "r")

    for linea in fichero:
        campos = linea.split(";")
        isbn = int(campos[0])
        titulo = campos[1]
        autoria = campos[2]
        libro = { "isbn": isbn, "titulo": titulo, "autoria": autoria } 
        libros.append(libro)

    fichero.close()

def crear_prestamos(libros, usuarios):
    resultado = {}

    for i in range(1000):
        usuario = random.choice(usuarios)
        libro = random.choice(libros)
        if (usuario not in resultado):
            resultado[usuario] = [ libro ]
        else:
            resultado[usuario] = resultado[usuario] + [ libro ]

    return resultado

def usuario_mas_prestamos(prestamos):
    resultado = ""
    candidato_clave = ""
    candidato_valor = []

    for clave in prestamos:
        valor = prestamos[clave]
        if (len(valor) > len(candidato_valor)):
            candidato_clave = clave
            candidato_valor = valor

    resultado = candidato_clave

    return resultado

def guardar_prestamos(prestamos):
    fichero = open("prestamos.csv", "w")

    for clave in prestamos:
        valor = prestamos[clave]
        fichero.write(f"{clave};{len(valor)};\n")

    fichero.close()

def crear_tabla():
    resultado = []

    for i in range(10):
        fila = []
        for j in range(10):
            aleatorio = random.randint(1, 6)
            fila.append(aleatorio)
        resultado.append(fila)

    return resultado

def limpiar_tabla(tabla, n):
    resultado = []

    for fila in tabla:
        f = []
        for numero in fila:
            if (numero != n):
                f.append(numero)
        resultado.append(f)

    return resultado

libros = []
usuarios = ['garaizar', 'bosanz', 'mlguenaga', 'ablago', 'jfajardo']
cargar_libros(libros)
prestamos = crear_prestamos(libros, usuarios)

print(usuario_mas_prestamos(prestamos)) 

guardar_prestamos(prestamos)