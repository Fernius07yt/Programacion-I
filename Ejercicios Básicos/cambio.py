# Entrada de datos del usuario
coste: float = float(input("Introduce el coste de la compra: "))
pagado: float = float(input("Introduce el dinero que has pagado: "))

# Cálculo de la devolución en centimos y de la división de monedas
devolucion_centimos: int = int(pagado * 100 - coste * 100)

# División de monedas en euros y centimos
monedas_2_euros: int = devolucion_centimos // 200
monedas_1_euro: int = (devolucion_centimos % 200) // 100
monedas_50_centimos: int = (devolucion_centimos % 100) // 50
monedas_20_centimos: int = (devolucion_centimos % 50) // 20
monedas_10_centimos: int = (devolucion_centimos % 20) // 10
monedas_5_centimos: int = (devolucion_centimos % 10) // 5
monedas_2_centimos = (devolucion_centimos % 5) // 2
monedas_1_centimos = (devolucion_centimos % 2) // 1

# Salida de resultados
print(f"\nCoste: {coste} euros")
print(f"Pagado: {pagado} euros")
print(f"Devolución: {devolucion_centimos / 100 :.2f} euros")

print(f"\nMonedas de 2 euros: {monedas_2_euros:.0f}")
print(f"Monedas de 1 euro: {monedas_1_euro:.0f}")
print(f"Monedas de 50 centimos: {monedas_50_centimos:.0f}")
print(f"Monedas de 20 centimos: {monedas_20_centimos:.0f}")
print(f"Monedas de 10 centimos: {monedas_10_centimos:.0f}")
print(f"Monedas de 5 centimos: {monedas_5_centimos:.0f}")
print(f"Monedas de 2 centimos: {monedas_2_centimos:.0f}")
print(f"Monedas de 1 centimo: {monedas_1_centimos:.0f}")