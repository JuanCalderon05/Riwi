dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))
cociente = 0
while dividendo >= divisor:
    dividendo -= divisor
    cociente += 1

print("La divicion es:", cociente)
