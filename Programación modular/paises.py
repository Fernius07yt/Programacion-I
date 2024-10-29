paises = {
    "Francia": 67345453,
    "Alemania": 81345345,
    "España": 47123123,
    "Irlanda": 3234211,
    "Islandia": 350223
}

for clave in paises:
    valor = paises[clave]
    print(f"pais: {clave}, poblacion: {valor}")

print(paises.keys())
print(paises.values())

paises = {
    "Francia": 67345453,
    "Alemania": 81345345,
    "España": 47123123,
    "Irlanda": 3234211,
    "Islandia": 350223
}

mayor_pais = ""
mayor_pob = 0

for clave in paises:
    valor = paises[clave]

    if (valor > mayor_pob):
        mayor_pob = valor
        mayor_pais = clave

print(f"El país con mayor población es {mayor_pais}")