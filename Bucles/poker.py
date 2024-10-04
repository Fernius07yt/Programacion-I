# Introduce una lista con todas las cartas y palos del poker
cartas = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
palos = ["Corazones", "Diamantes", "Treboles", "Picas"]

# Imprime todas las cartas y palos del poker en una sola línea, separados por un espacio
for palo in palos:
    for carta in cartas:
        print(f"{carta} de {palo}")