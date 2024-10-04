# Pide al usuario que introduzca su nota 
nota: float = float(input("¿Cual es tu nota? "))

# Mientras la nota no esté entre 0 y 10, muestra un mensaje de error y pide que introduzca una nueva nota.
while (nota < 0) or (nota > 10):
    print("Introduce una nota válida (entre 0 y 10).")
    nota = float(input("¿Cual es tu nota? "))

# Depende de la nota, muestra un mensaje con el resultado.
if nota < 5: 
    print("Suspendido.")
elif 5 <= nota < 7:
    print("Bien.")
elif 7 <= nota < 9:
    print("Notable.")
elif 9 <= nota <= 10:
    print("Sobresaliente.")