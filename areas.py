import math

def area_cuadrado(lado):
    return lado ** 2

def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) / 2) * altura

def area_rectangulo(base, altura):
    return base * altura

def calcular_area():

    print("Seleccione la figura de la que desea calcular el área:")

    print("1. Cuadrado")
    print("2. Círculo")
    print("3. Triángulo")
    print("4. Trapecio")
    print("5. Rectángulo")
    print("6. Salir")

    opcion = int(input("Ingrese el número de la figura: "))
    if opcion == 1:
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))
        print("El área del cuadrado es:", area_cuadrado(lado))

    elif opcion == 2:
        radio = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es:", area_circulo(radio))

    elif opcion == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es:", area_triangulo(base, altura))

    elif opcion == 4:
        base_mayor = float(input("Ingrese la longitud de la base mayor del trapecio: "))
        base_menor = float(input("Ingrese la longitud de la base menor del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        print("El área del trapecio es:", area_trapecio(base_mayor, base_menor, altura))

    elif opcion == 5:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print("El área del rectángulo es:", area_rectangulo(base, altura))

    else:
        print("Opción inválida")

calcular_area()
