suma_pares = 0
suma_impares = 0
cantidad_pares = 0
cantidad_impares = 0
numero = float(input("Ingrese un número: "))
while numero != 0:
    if numero % 2 == 0:
        suma_pares += numero
        cantidad_pares += 1
    if numero % 2 != 0:
        suma_impares += numero
        cantidad_impares += 1
    numero = float(input("Ingrese OTRO numero: "))
if cantidad_pares != 0:
    promedio_pares = suma_pares / cantidad_pares
else:
    promedio_pares = 0
if cantidad_impares != 0:
    promedio_impares = suma_impares / cantidad_impares
else:
    promedio_impares = 0
print("Hay:",cantidad_pares,"numeros pares y su promedio es:", promedio_pares)
print("Hay:",cantidad_impares,"numeros pares y su promedio es:", promedio_impares)
