# Solicita al usuario que introduzca una frase
frase = input("Escribe una frase:")

# Inicializa la variable para contar los espacios en blanco a 0  (cada espacio es un caracter)
espacios = 0

# Recorre cada caracter de la frase y si encuentra un espacio, incrementa el contador de espacios en blanco.
for caracter in frase:

    # Si el caracter es un espacio, incrementa el contador de espacios en blanco.
    if caracter == " ":
        espacios += 1

# Muestra cuantos espacios hay en la frase 
print(f"La frase tiene {espacios} espacios.")