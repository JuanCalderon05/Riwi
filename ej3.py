contador = 0
numero = 200

while numero <= 432:
    if numero % 2 == 0 and numero % 7 == 0:
        contador += 1
    numero += 1

print("La cantidad de números pares múltiplos de 7 entre 200 y 432 es:", contador)
