def binario_a_decimal(binario):
    resultado = 0
    alreves = ""

    for digito in binario:
        alreves = digito + alreves

    factor = 1

    for digito in alreves:
        resultado = resultado + int(digito) * factor
        factor = factor * 2

    return resultado

# Función que traduce un entero a binario (str)
# Importante: solamente funciona con enteros >= 0

def decimal_a_binario(decimal):
    resultado = ""

    resto = decimal % 2
    resultado = str(resto) + resultado
    cociente = decimal // 2
    
    while (cociente > 0):
        resto = cociente % 2
        resultado = str(resto) + resultado
        cociente = cociente // 2

    return resultado

print(binario_a_decimal("1010"))
print(decimal_a_binario(-10))