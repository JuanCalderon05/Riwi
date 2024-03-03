productos = []
ventas = []

def agregar_producto(nombre, precio, cantidad):
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})

def obtener_producto(nombre):
    for producto in productos:
        if producto['nombre'] == nombre:
            return producto
    return None

def vender_producto(nombre, cantidad):
    producto = obtener_producto(nombre)
    if producto and producto['cantidad'] >= cantidad:
        producto['cantidad'] -= cantidad
        ventas.append({'nombre': nombre, 'cantidad': cantidad, 'precio': producto['precio'], 'total': cantidad * producto['precio']})
        return True
    else:
        return False

def mostrar_productos():
    print("Lista de productos en el inventario:")
    for i, producto in enumerate(productos):
        print(f"{i+1}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")



def cuerpo():
    while True:

        print("\nMENU DE OPCIONES")
        print("1. Agregar nuevo producto al inventario")
        print("2. Ver lista de productos en el inventario")
        print("3. Vender producto")
        print("4. Salir")

        opcion = int(input("Seleccione por favor una opcion: "))

        if  opcion == 4:
            print("Saliendo......\n")
            break

        if opcion == 1:
            nombre = input("Ingrese un producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad disponible del producto: "))
            agregar_producto(nombre, precio, cantidad)

        elif opcion == 2:
            mostrar_productos()

        elif opcion == 3:
            nombre = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad de productos a vender: "))
            if vender_producto(nombre, cantidad):
                print("Producto Vendido")
            else:
                print("No hay suficiente cantidad en stock para realizar la venta")
cuerpo()

