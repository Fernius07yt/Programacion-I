# Diccionarios para "etiquetar" datos
cancion = [ "Anuel AA", "Amanece", 234 ]
titulo = cancion[1]

cancion = { 
    "artista": "Anuel AA", 
    "titulo": "Amanece", 
    "duracion": 234 
}
titulo = cancion["titulo"]

# Diccionarios con datos en la clave y datos en el valor

# Caso habitual 1: contar cosas -> cada valor es un contador

poblaciones = {
    "Francia": 67234234,
    "Alemania": 87645643,
    "España": 48242324
}

for clave in poblaciones:
    valor = poblaciones[clave]

# Caso habitual 2: agrupar cosas -> cada valor es una lista

amistades = {
    "pablo": ["borja", "ana", "mluz"],
    "borja": ["ana", "mluz"]
}