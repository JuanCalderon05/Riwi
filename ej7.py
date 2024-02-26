suma = 0
contador = 0

while contador < 5:
    nota_ = float(input("Ingrese su nota: "))
    suma += nota_
    contador += 1
promedio = suma / 5

print("El promedio de las 5 notas es:", promedio)
