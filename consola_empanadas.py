from datetime import datetime

def mostrar_empanada(empanada: dict) -> None:
    nombre = empanada["nombre"]
    precio = empanada["precio"]
    vegana = empanada["vegana"]
    ingredientes = empanada["ingredientes"]
    toppings = empanada["toppings"]
    rating = empanada["rating"]
    unidades_vendidas = empanada["unidades_vendidas"]
    proxima_fecha_entrega = empanada["proxima_fecha_entrega"]

    print("Nombre: " + nombre +
            "\nPrecio: " + str(precio) +
            "\n¿Es Vegana?: " + str(vegana) +
            "\nIngredientes: " + str(ingredientes) +
            "\nToppings recomendados: " + str(toppings) +
            "\nRating: " + str(rating) +
            "\nUnidades vendidas: " + str(unidades_vendidas) +
            "\nProxima fecha entrega: " + str(proxima_fecha_entrega))


def ejecutar_buscar_empanada_por_nombre(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    nombre_buscar = input("Ingrese el nombre de la empanada a buscar: ")

    empanadas = [e1, e2, e3, e4]
    empanada_encontrada = None

    for empanada in empanadas:
        if empanada["nombre"].lower() == nombre_buscar.lower():
            empanada_encontrada = empanada
            break

    if empanada_encontrada:
        print(f"{empanada_encontrada['nombre']} cuesta {empanada_encontrada['precio']} y tiene {empanada_encontrada['ingredientes']}")
    else:
        print("No se encontró la empanada")


def ejecutar_buscar_empanada_mas_ganancias(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    empanadas = [e1, e2, e3, e4]
    empanada_con_mas_ganancias = max(empanadas, key=lambda x: x["precio"] * x["unidades_vendidas"])
    ganancias = empanada_con_mas_ganancias["precio"] * empanada_con_mas_ganancias["unidades_vendidas"]
    print(f"La empanada con más ganancias es {empanada_con_mas_ganancias['nombre']} con ganancias de {ganancias}")


def ejecutar_buscar_empanadas_por_ingrediente(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    ingrediente_buscar = input("Ingrese el ingrediente a buscar: ")
    
    empanadas = [e1, e2, e3, e4]
    empanadas_con_ingrediente = []
    
    for empanada in empanadas:
        if ingrediente_buscar.lower() in empanada["ingredientes"].lower():
            empanadas_con_ingrediente.append(empanada["nombre"])
    
    if empanadas_con_ingrediente:
        print(f"Las empanadas que contienen {ingrediente_buscar} son: {', '.join(empanadas_con_ingrediente)}")
    else:
        print(f"No se encontró ninguna empanada con {ingrediente_buscar}")


def ejecutar_buscar_empanada_con_mejor_rating_por_topping(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    topping_buscar = input("Ingrese el topping a buscar: ")

    empanadas = [e1, e2, e3, e4]
    empanada_mejor_rating = None
    max_rating = 0

    for empanada in empanadas:
        if topping_buscar.lower() in empanada["toppings"].lower():
            if empanada["rating"] > max_rating:
                max_rating = empanada["rating"]
                empanada_mejor_rating = empanada

    if empanada_mejor_rating:
        print(f"La empanada con mejor rating con {topping_buscar} es {empanada_mejor_rating['nombre']} con {empanada_mejor_rating['rating']} de rating")
    else:
        print(f"No se encontró ninguna empanada con {topping_buscar}")


def ejecutar_calcular_promedio_rating_empanadas(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    empanadas = [e1, e2, e3, e4]
    total_rating = 0
    cantidad_empanadas = 0

    for empanada in empanadas:
        if empanada["vegana"]:
            total_rating += empanada["rating"]
            cantidad_empanadas += 1

    if cantidad_empanadas > 0:
        promedio_rating = total_rating / cantidad_empanadas
        print(f"El promedio de rating de las empanadas es {promedio_rating:.2f}")
    else:
        print("No hay empanadas veganas para calcular el promedio de rating")


def ejecutar_comparar_rating_empanadas_veganas_y_no_veganas(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    empanadas_veganas = [e1, e2, e3, e4]
    empanadas_no_veganas = []

    for empanada in empanadas_veganas:
        if not empanada["vegana"]:
            empanadas_no_veganas.append(empanada)

    promedio_rating_veganas = sum(empanada["rating"] for empanada in empanadas_veganas) / len(empanadas_veganas)
    promedio_rating_no_veganas = sum(empanada["rating"] for empanada in empanadas_no_veganas) / len(empanadas_no_veganas)

    if promedio_rating_veganas > promedio_rating_no_veganas:
        print("El promedio de rating de las empanadas veganas es mayor que el de las no veganas")
    elif promedio_rating_veganas < promedio_rating_no_veganas:
        print("El promedio de rating de las empanadas no veganas es mayor que el de las veganas")
    else:
        print("El promedio de rating de las empanadas veganas y no veganas es el mismo")


def ejecutar_modificar_rating_y_toppings(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    nombre_buscar = input("Ingrese el nombre de la empanada a modificar: ")

    empanadas = [e1, e2, e3, e4]
    empanada_modificada = None

    for empanada in empanadas:
        if empanada["nombre"].lower() == nombre_buscar.lower():
            empanada_modificada = empanada
            break

    if empanada_modificada:
        nuevo_rating = float(input("Ingrese el nuevo rating: "))
        nuevos_toppings = input("Ingrese los nuevos toppings (separados por coma): ")
        empanada_modificada["rating"] = nuevo_rating
        empanada_modificada["toppings"] = nuevos_toppings
        print("Se ha modificado exitosamente la empanada")
    else:
        print("No se encontró la empanada")


def ejecutar_calcular_tiempo_proxima_fecha_entrega(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    nombre_buscar = input("Ingrese el nombre de la empanada: ")

    empanadas = [e1, e2, e3, e4]
    empanada_encontrada = None

    for empanada in empanadas:
        if empanada["nombre"].lower() == nombre_buscar.lower():
            empanada_encontrada = empanada
            break

    if empanada_encontrada:
        fecha_ingresada_str = input("Ingrese la fecha en formato YYYYMMDD: ")
        fecha_ingresada = datetime.strptime(fecha_ingresada_str, "%Y%m%d")
        proxima_fecha_entrega = datetime.strptime(str(empanada_encontrada["proxima_fecha_entrega"]), "%Y%m%d")

        if fecha_ingresada > proxima_fecha_entrega:
            print(f"La entrega de {empanada_encontrada['nombre']} ya pasó")
        else:
            tiempo_restante = proxima_fecha_entrega - fecha_ingresada
            anos_restantes = tiempo_restante.days // 365
            meses_restantes = (tiempo_restante.days % 365) // 30
            dias_restantes = (tiempo_restante.days % 365) % 30
            print(f"Faltan {anos_restantes} años, {meses_restantes} meses y {dias_restantes} días entre la fecha {fecha_ingresada_str} y la próxima fecha de entrega de {empanada_encontrada['nombre']}")
    else:
        print("No se encontró la empanada")


def iniciar_aplicacion() -> None:
    empanada1 = {
        "nombre": "Empanada Carnívora Multicarne",
        "precio": 2700,
        "vegana": False,
        "ingredientes": "Carne de res, Carne de cerdo, Pollo desmenuzado, Huevo Cebolla, Pimiento",
        "toppings": "Salsa de chimichurri, Ají",
        "rating": 4.6,
        "unidades_vendidas": 160,
        "proxima_fecha_entrega": 20240306
    }

    empanada2 = {
        "nombre": "Empanada de los Sabores del Huerto",
        "precio": 3000,
        "vegana": True,
        "ingredientes": "Champiñones, Cebolla, Pimiento, Tomate, Aceitunas",
        "toppings": "Salsa de ajo, Salsa de mostaza",
        "rating": 4.3,
        "unidades_vendidas": 120,
        "proxima_fecha_entrega": 20240309
    }

    empanada3 = {
        "nombre": "Empanada de Pollo",
        "precio": 2550,
        "vegana": False,
        "ingredientes": "Pollo desmenuzado, Cebolla, Pimiento, Tomate",
        "toppings": "Ají, Salsa de ajo",
        "rating": 4.5,
        "unidades_vendidas": 200,
        "proxima_fecha_entrega": 20240208
    }

    empanada4 = {
        "nombre": "Empanada Vegana de Lentejas",
        "precio": 3200,
        "vegana": True,
        "ingredientes": "Lentejas, Cebolla, Pimiento, Tomate",
        "toppings": "Guacamole, Salsa de mostaza",
        "rating": 4.2,
        "unidades_vendidas": 100,
        "proxima_fecha_entrega": 20240518
    }

    ejecutando = True
    while ejecutando:
        print("\nEmpanadas existentes\n" + ("-"*50))
        print("Empanada 1\n")
        mostrar_empanada(empanada1)
        print("-"*50)

        print("Empanada 2\n")
        mostrar_empanada(empanada2)
        print("-"*50)

        print("Empanada 3\n")
        mostrar_empanada(empanada3)
        print("-"*50)

        print("Empanada 4\n")
        mostrar_empanada(empanada4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(
            empanada1, empanada2, empanada3, empanada4)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(e1: dict, e2: dict, e3: dict, e4: dict) -> bool:
    print("Menu de opciones")
    print(" 1 - Buscar empanada por nombre")
    print(" 2 - Buscar empanada con más ganancias")
    print(" 3 - Buscar empanadas por ingrediente")
    print(" 4 - Buscar empanada con mejor rating por topping")
    print(" 5 - Calcular promedio de rating de las empanadas (veganas o no veganas)")
    print(" 6 - Comparar promedio de rating de las empanadas veganas y no veganas")
    print(" 7 - Modificar rating y toppings de una empanada")
    print(" 8 - Calcular los años, meses y dias para la proxima fecha de entrega de una empanada")
    print(" 9 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_empanada_por_nombre(
            e1, e2, e3, e4)
    elif opcion_elegida == "2":
        ejecutar_buscar_empanada_mas_ganancias(
            e1, e2, e3, e4)
    elif opcion_elegida == "3":
        ejecutar_buscar_empanadas_por_ingrediente(
            e1, e2, e3, e4)
    elif opcion_elegida == "4":
        ejecutar_buscar_empanada_con_mejor_rating_por_topping(
            e1, e2, e3, e4)
    elif opcion_elegida == "5":
        ejecutar_calcular_promedio_rating_empanadas(
            e1, e2, e3, e4)
    elif opcion_elegida == "6":
        ejecutar_comparar_rating_empanadas_veganas_y_no_veganas(
            e1, e2, e3, e4)
    elif opcion_elegida == "7":
        ejecutar_modificar_rating_y_toppings(
            e1, e2, e3, e4)
    elif opcion_elegida == "8":
        ejecutar_calcular_tiempo_proxima_fecha_entrega(
            e1, e2, e3, e4)
    elif opcion_elegida == "9":
        continuar_ejecutando = False
    else:
        print("La opción " + opcion_elegida + " no es una opción válida.")
    return continuar_ejecutando


iniciar_aplicacion()
