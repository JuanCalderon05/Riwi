positivos = 0
negativos = 0
ceros = 0
while True:
    numero = float(input("Ingrese un número: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1 
    opcion = input("¿Desea ingresar otro número? (si/no): ")
    if opcion.lower() != "si":
        break
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("Cantidad de ceros:", ceros)
