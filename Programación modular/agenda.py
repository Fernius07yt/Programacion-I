#contacto1 = {
#    "nombre": "Pablo",
#    "telefono": "667 547 567"
#}

def mostrar_contactos(contactos):
    print("Contactos de la agenda...")
    for pos, contacto in enumerate(contactos):
        print(f"{pos} - {contacto}")

def anadir_contacto(contactos):
    print("Introduce los datos del contacto...")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    contacto = { "nombre": nombre, "telefono": telefono }
    contactos.append(contacto)

def borrar_contacto(contactos):
    mostrar_contactos(contactos)
    pos = int(input("Elige contacto: "))
    contacto = contactos[pos]
    contactos.remove(contacto)

def modificar_contacto(contactos):
    borrar_contacto(contactos)
    anadir_contacto(contactos)

def guardar_contactos(contactos):
    fichero = open("agenda.csv", "w")

    for contacto in contactos:
        # nombre;telefono;\n
        fichero.write(f"{contacto['nombre']}{contacto['telefono']};\n")

    fichero.close()

def cargar_contactos (contactos):
    fichero = open("agenda.csv", "r")

    for linea in fichero:
        campos = linea.split(";") # "Pablo;12345678;\n" -> [ "Pablo", "12345678", "\n"]
        nombre = campos[0]
        telefono = campos[1]
        contacto = { "nombre": nombre, "telefono": telefono}
        contactos.append(contacto)

    fichero.close()

contactos = []

terminar = False

while (not terminar):
    print("Agenda:")
    print("1) Mostrar contactos")
    print("2) Añadir contacto nuevo")
    print("3) Borrar contacto")
    print("4) Modificar contacto")
    print("5) Guardar agenda")
    print("6) Cargar agenda")
    print("0) Salir")
    opcion = input("¿Opción? ")

    if (opcion == "1"):
        mostrar_contactos(contactos)
    elif (opcion == "2"):
        anadir_contacto(contactos)
    elif (opcion == "3"):
        borrar_contacto(contactos)
    elif (opcion == "4"):
        modificar_contacto(contactos)
    elif (opcion == "5"):
        guardar_contactos(contactos)
    elif (opcion == "6"):
        cargar_contactos(contactos)
    elif (opcion == "0"):
        terminar = True
    