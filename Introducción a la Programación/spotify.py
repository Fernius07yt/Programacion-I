"""
Gestión de listas de música (Spotify)

Elige una opción:
1) Mostrar canciones
2) Añadir una canción
3) Eliminar una canción
4) Mostrar la canción más larga
5) Mostrar las canciones favoritas
¿Opción? 1
Lista de canciones:
1    Blinding Lights de The Weeknd (200s)
2    Levitating de Dua Lipa (203s)
3    Save Your Tears de The Weeknd (215s)
...

Elige una opción:
1) Mostrar canciones
2) Añadir una canción
3) Eliminar una canción
4) Mostrar la canción más larga
5) Mostrar las canciones favoritas
¿Opción? 2
Añadiendo una canción nueva...
Título: a
Autoría: b
Duración: 1
Favorita (s/n): s

Elige una opción:
1) Mostrar canciones
2) Añadir una canción
3) Eliminar una canción
4) Mostrar la canción más larga
5) Mostrar las canciones favoritas
¿Opción? 3
Lista de canciones:
1    Blinding Lights de The Weeknd (200s)
2    Levitating de Dua Lipa (203s)
3    Save Your Tears de The Weeknd (215s)
...
¿Qué canción quieres borrar?
2

Elige una opción:
1) Mostrar canciones
2) Añadir una canción
3) Eliminar una canción
4) Mostrar la canción más larga
5) Mostrar las canciones favoritas
¿Opción? 4
La canción más larga de la lista es:
drivers license de Olivia Rodrigo (242s)

Elige una opción:
1) Mostrar canciones
2) Añadir una canción
3) Eliminar una canción
4) Mostrar la canción más larga
5) Mostrar las canciones favoritas
¿Opción? 5
Lista de canciones favoritas:
1    Blinding Lights de The Weeknd (200s)
2    Save Your Tears de The Weeknd (215s)
3    Montero (Call Me By Your Name) de Lil Nas X (137s)
4    Bad Habits de Ed Sheeran (231s)
5    Good 4 U de Olivia Rodrigo (178s)

"""
def mostrar_cancion(cancion:list) -> None:
	"""recibe una canción ["titulo", "autoria", duracion, favorita] y la muestra por pantalla"""
	print(f"{cancion[0]} de {cancion[1]} ({cancion[2]}s)")
	
def mostrar_canciones(canciones:list) -> None:
	"""recibe una lista de canciones las muestra por pantalla"""
	print("Lista de canciones:")
	for i in range(len(canciones)):
		print(i+1, end="\t")
		mostrar_cancion(canciones[i])

def anadir_cancion(canciones:list) -> list:
	"""añade una canción ["titulo", "autoria", duracion, favorita] a la lista de canciones recibida"""
	# Pedimos los datos
	titulo:str = input("Titulo: ")
	artista:str = input("Artista: ")
	duracion:int = int(input("Duracion: "))
	favorita:str = input("¿Es favorita? (s/n): ")
	fav:bool = False
	if (favorita.lower() == "s"):
		fav = True
	# Creamos una nueva cancion
	cancion:list = [titulo, artista, duracion, fav]
	# Añadir la nueva canción a la lista de canciones
	# lista = lista + elemento -> ERROR
	# lista = lista + [elemento] -> OK
	# lista.append(elemento)
	canciones = canciones + [cancion]
	# canciones.append(cancion)
	# Devolvemos al programa principal la lista de canciones modificada
	return canciones

def eliminar_cancion(canciones:list) -> list:
	"""elimina una canción de la lista de canciones recibida"""
	mostrar_canciones(canciones)
	numero:int = int(input("¿Qué cancion quieres eliminar? "))
	cancion = canciones[numero-1]
	canciones.remove(cancion)
	return canciones

def cancion_mas_larga(canciones:list) -> list:
	"""devuelve la canción más larga de la lista"""
	resultado:list = canciones[0]
	for cancion in canciones:
		if (cancion[2] > resultado[2]):
			resultado = cancion
	return resultado

def cancion_con_titulo_mas_largo(canciones:list) -> list:
	"""devuelve la canción más larga de la lista"""
	resultado:list = canciones[0]
	for cancion in canciones:
		if (len(cancion[0]) > len(resultado[0])):
			resultado = cancion
	return resultado

def canciones_favoritas(canciones:list) -> list:
	"""devuelve las canciones favoritas de entre la lista de canciones recibida"""
	resultado:list = []
	for cancion in canciones:
		if (cancion[3] == True):
			resultado = resultado + [cancion]
	return resultado

def canciones_cortas(canciones:list) -> list:
	"""devuelve las canciones con duracion < 100 de entre la lista de canciones recibida"""
	resultado:list = []
	for cancion in canciones:
		if (cancion[2] < 100):
			resultado = resultado + [cancion]
	return resultado


lista = [
    ["Blinding Lights", "The Weeknd", 200, True],
    ["Levitating", "Dua Lipa", 203, False],
    ["Save Your Tears", "The Weeknd", 215, True],
    ["Peaches", "Justin Bieber", 198, False],
    ["Montero (Call Me By Your Name)", "Lil Nas X", 137, True],
    ["Stay", "The Kid LAROI & Justin Bieber", 141, False],
    ["Bad Habits", "Ed Sheeran", 231, True],
    ["drivers license", "Olivia Rodrigo", 242, False],
    ["Good 4 U", "Olivia Rodrigo", 178, True],
    ["Shivers", "Ed Sheeran", 207, False],
]

while (True):
	print("Elige una opción:")
	print("1) Mostrar canciones")
	print("2) Añadir una canción")
	print("3) Eliminar una canción")
	print("4) Mostrar la canción más larga")
	print("5) Mostrar las canciones favoritas")
	print("0) Salir")
	opcion:str = input("¿Opción? ")
	if (opcion == "0"):
		break
	elif (opcion == "1"):
		mostrar_canciones(lista)
	elif (opcion == "2"):
		lista = anadir_cancion(lista)
	elif (opcion == "3"):
		lista = eliminar_cancion(lista)
	elif (opcion == "4"):
		mostrar_cancion(cancion_mas_larga(lista))
	elif (opcion == "5"):
		mostrar_canciones(canciones_favoritas(lista))
	else:
		print("Opción no disponible")

