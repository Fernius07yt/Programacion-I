# Solicita al usuario que introduzca una frase en minusculas
frase = input("Escribe una frase en minusculas: ")

# Define las vocales en minusculas y crea una cadena vacia para almacenar la frase modificada
vocales = "aeiou"
nueva_frase = ""

# Recorre la frase y reemplaza las vocales con asteriscos, dejando las demás letras intactas
for letra in frase:

    # Si la letra no es una vocal, la añade a la cadena nueva_frase en su lugar
    if letra in vocales:
        nueva_frase += "*"
        continue
    
    # Si la letra es una vocal, la añade a la cadena nueva_frase en su lugar
    nueva_frase += letra

# Muestra la frase modificada con asteriscos en lugar de las vocales
print(nueva_frase)