# Entrada
coste = 18.78
pagado = 20

# Procesamiento
centimos = int(pagado * 100 - coste * 100) 
monedas2e = centimos // 200
resto = centimos % 200
monedas1e = resto // 100
resto = resto % 100
monedas50c = resto // 50
resto = resto % 50
monedas20c = resto // 20
resto = resto % 20
monedas10c = resto // 10
resto = resto % 10
monedas5c = resto // 5
resto = resto % 5
monedas2c = resto // 2
resto = resto % 2

# Salida
print(f"Coste: {coste}")
print(f"Pagado: {pagado}")
print(f"Devolver: {centimos/100}")
print(f"{monedas2e} monedas de 2 euros")
print(f"{monedas1e} monedas de 1 euros")
print(f"{monedas50c} monedas de 50 c")
print(f"{monedas20c} monedas de 20 c")
print(f"{monedas10c} monedas de 10 c")
print(f"{monedas5c} monedas de 5 c")
print(f"{monedas2c} monedas de 2 c")
print(f"{resto} monedas de 1 c ")