# Lista
jugadora = [ "Bonmati", [77, 45, 92], [23, 1.67]]

fuerza = jugadora[1][1] # 45 de fuerza

# Diccionario como si fuera una lista
jugadora = {
    "0": "Bonmatí",
    "1": {
        "0": 77,
        "1": 45,
        "2": 92
    },
    "2": {
        "0": 23,
        "1": 1.67
    }
}

# Diccionario correctamente etiquetado
jugadora = {
    "nombre": "Bonmatí",
    "habilidades": {
        "velocidad": 77,
        "fuerza": 45,
        "regate": 92
    },
    "caracteristicas": {
        "edad": 23,
        "altura": 1.67
    }
}

fuerza = jugadora["habilidades"]["fuerza"]
