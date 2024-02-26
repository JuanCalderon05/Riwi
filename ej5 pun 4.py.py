contador = 0
suma = 0
numero = 100

while numero <= 330:
    if numero % 2 == 0:
        contador += 1
        suma += numero
    numero += 1

if contador != 0:
    promedio = suma / contador
    print("El promedio de los números pares entre 100 y 330 es:", promedio)
