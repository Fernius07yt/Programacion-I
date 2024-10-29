# Entrada
edad:int = int(input("Edad: "))
# es_miercoles:bool = input("¿Es miércoles? (s/n) ") == "s" 
es_miercoles:bool = False

respuesta = input("¿Es miércoles? (s/n) ")
if (respuesta == "s"):
    es_miercoles = True

# Procesamiento
precio:float = 10

if (es_miercoles or edad < 5): # tarifa gratis?
    precio = 0
elif (edad < 18): # tarifa joven?
    precio = 5
elif (edad >= 65): # tarifa senior?
    precio = 7

# Salida
print(f"Precio: {precio} euros")