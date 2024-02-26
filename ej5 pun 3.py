contador = 0
suma = 0
numero = 200

while numero <= 432:
    if numero % 2 == 0 and numero % 7 == 0:
        contador += 1
        suma += numero
    numero += 1

if contador != 0:
    promedio = suma / contador
    print("El promedio de los números pares múltiplos de 7 entre 200 y 432 es:", promedio)
