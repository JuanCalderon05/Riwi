import os

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

import sys

def calcular_materiales_pared():
    clear_console()
    
    try:
        longitud = float(input("Ingrese la longitud de la pared (en metros): "))
        altura = float(input("Ingrese la altura de la pared (en metros): "))
        
        if longitud <= 0 or altura <= 0:
            print("Error: La longitud y la altura deben ser valores numéricos positivos.")
            return
    except ValueError:
        print("Error: La longitud y la altura deben ser valores numéricos positivos.")
        return

    area_pared = longitud * altura

    largo_ladrillo = 0.2
    ancho_ladrillo = 0.1
    espacio_perdido = 0.05


    cantidad_ladrillos = (area_pared / (largo_ladrillo * ancho_ladrillo)) * (1 + espacio_perdido)

    try:
        mortero_por_metro_cuadrado = float(input("Ingrese la cantidad de mortero por metro cuadrado (en metros cúbicos): "))
        if mortero_por_metro_cuadrado <= 0:
            print("Error: La cantidad de mortero debe ser un valor numérico positivo.")
            return
    except ValueError:
        print("Error: La cantidad de mortero debe ser un valor numérico positivo.")
        return

    mortero_total = area_pared * mortero_por_metro_cuadrado

    print("\nCantidad total de ladrillos necesarios:", round(cantidad_ladrillos, 2))
    print("Cantidad de mortero requerida:", round(mortero_total, 2), "metros cúbicos")

calcular_materiales_pared()
