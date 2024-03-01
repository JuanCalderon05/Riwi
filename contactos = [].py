import os

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

contactos = []

def mostrar_menu ():
    print("MENU DE OPCIONES")
    print("\t1. Agregar contacto")
    print("\t2. Ver contactos")
    print("\t3. Buscar contactos")
    print("\t4. Eliminar contactos")
    print("\t5. Salir")

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = int(input("Ingresa el numero de telefono del contacto:"))
    contacto = {"nombre": nombre, "telefono":telefono}
    contactos.append(contacto)

def ver_contacto():
    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']}, Telefono: {contacto['telefono']}")

def  buscar_contacto():
    nombre = input("Digite el nombre del contacto que desea buscar: ")
    encontrado = False
    for contacto in contactos:
        if contacto ["nombre"] == nombre:
            print(f"Nombre: {contacto['nombre']}, Telefono: {contacto['telefono']}")
            encontrado = True
    if not encontrado:
        print("contacto no encontrado")

def eliminar_contacto():
    nombre = input ("Ingrese el nombre del contacto a eliminar: ")
    for i, contacto in enumerate(contactos):
        if  contacto["nombre"] == nombre:
            del contactos[i]
            print("Contacto eliminado")
            break
    else:
        print("Contacto no encontrado")

while True:
    mostrar_menu()

    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        agregar_contacto()
    elif opcion == 2:
        ver_contacto()
    elif opcion == 3:
        buscar_contacto()
    elif opcion == 4:
        eliminar_contacto()
    elif opcion == 5:
        print("!HAS SALIDO!")
        break
    else:
        print("Opcion invalida, intentalo de nuevo")