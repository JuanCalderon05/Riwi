suma = 0
cantidad_multiplos = 0

while True:
    numero = int(input("Ingrese un número (Ingrese 0 para terminar): "))
    if numero == 0:
        break
    if numero % 7 == 0:
        suma += numero
        cantidad_multiplos += 1

if cantidad_multiplos != 0:
    promedio = suma / cantidad_multiplos
    print("El promedio de los números múltiplos de 7 es:", promedio)
else:
    print("No se ingresaron números múltiplos de 7.")
