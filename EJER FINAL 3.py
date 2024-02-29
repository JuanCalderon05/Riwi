P_cocina = []
C_product = []
options = True

while options:
    print("INGRESE POR FAVOR LA LISTA DE PRODUCTOS A SUMINISTRAR")

    print("\nOPCIONES:\n")
    print("1.\t AGREGAR PRODUCTOS")
    print("2.\t VER PRODUCTOS ACTUALES")
    print("3.\t REGISTRAR GASTO DE PRODUCTO")

    select = input("\nELIJA UNA OPCION: ")

    if select not in ['1', '2', '3']:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
        continue

    select = int(select)

    seguir_ingresando = True

    while seguir_ingresando:
        if select == 2:
            print("*************************************************")

            print("\nLISTA DE PRODUCTOS ACTUALES")
            print("NOMBRE / CANTIDAD")
            for product, cantidadP_ in zip(P_cocina, C_product):
                print("*************************************************")

                print(product, "/", cantidadP_)

                print("*************************************************")

        if select == 1:
            print("*************************************************")

            products_ = input("Ingresa un producto: ")
            cantidad_ = input("Cantidad de producto: ")

            print("*************************************************")

            if not cantidad_.isdigit():
                print("Cantidad no válida. Por favor, ingrese un número entero.")
                continue

            P_cocina.append(products_)
            C_product.append(int(cantidad_))

        if select == 3:
            print("*************************************************")

            product_gasto = input("Ingresa el producto que se ha gastado: ")
            cantidad_gasto = input("Ingresa la cantidad utilizada: ")

            print("*************************************************")

            if product_gasto not in P_cocina:
                print("El producto ingresado no está en el inventario.")
                continue

            index = P_cocina.index(product_gasto)
            cantidad_actual = C_product[index]

            if not cantidad_gasto.isdigit():
                print("Cantidad no válida. Por favor, ingrese un número entero.")
                continue

            cantidad_gasto = int(cantidad_gasto)

            if cantidad_gasto > cantidad_actual:
                print("La cantidad utilizada es mayor que la cantidad disponible en el inventario.")
                continue

            C_product[index] -= cantidad_gasto
            print(f"Se ha registrado el gasto de {cantidad_gasto} unidades de {product_gasto}.")

        o_t = input("\n¿Quieres ingresar otro producto / realizar otra acción? (s/Enter) \n")
        if o_t.lower() == 's':
            continue
        else:
            seguir_ingresando = False

    salir = input("\n¿Desea salir del programa? (s/Enter) \n")
    if salir.lower() == 's':
        break





    