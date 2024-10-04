# Entrada de datos del usuario de la edad y si es miercoles
edad: int = int(input("Introduce tu edad: "))
es_miercoles: str = input("¿Es miercoles? (s/n): ")

# Si es miercoles, el precio es de 0€ y no se calcula nada más
if (es_miercoles == "s"):
    print("Precio: 0€")

#Si no es miercoles, se calcula el precio según la edad
else:
    # Si la edad es mayor o igual que 5, el precio es de 0€
    if (edad <= 5): 
        print("Precio: 0€")

    # Si la edad está entre 6 y 17, el precio es de 5€
    elif (edad < 18):
        print("Precio: 5€")

    # Si la edad está entre 18 y 64, el precio es de 10€
    elif (edad >= 18) and (edad <= 64):
        print("Precio: 10€")
        
    # Si la edad es mayor que 64, el precio es de 7€
    else:
        print("Precio: 7€")