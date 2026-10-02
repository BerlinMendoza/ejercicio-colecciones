# Programa de registro de contactos
# Uso de colecciones de datos: Diccionario

# Diccionario con contactos registrados inicialmente
contactos = {
    "María": "0991234567",
    "Carlos": "0987654321",
    "Ana": "0976543210",
    "Pedro": "0965432109"
}


# Función para agregar un nuevo contacto
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")

    contactos[nombre] = telefono
    print("Contacto agregado correctamente.")


# Función para mostrar todos los contactos
def mostrar_contactos():
    if len(contactos) == 0:
        print("No hay contactos registrados.")
    else:
        print("\n--- LISTA DE CONTACTOS ---")

        for nombre, telefono in contactos.items():
            print("Nombre:", nombre, "| Teléfono:", telefono)


# Función para buscar un contacto
def buscar_contacto():
    nombre = input("Ingrese el nombre que desea buscar: ")

    if nombre in contactos:
        print("\nContacto encontrado:")
        print("Nombre:", nombre)
        print("Teléfono:", contactos[nombre])
    else:
        print("El contacto no se encuentra registrado.")


# Menú principal
while True:
    print("\n===== AGENDA DE CONTACTOS =====")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto()

    elif opcion == "2":
        mostrar_contactos()

    elif opcion == "3":
        buscar_contacto()

    elif opcion == "4":
        print("Programa finalizado. ¡Gracias!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")