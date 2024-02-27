suma = 0
numero = float(input("Ingrese un número: "))
count = 0

while numero != 0:
    suma += numero
    numero = float(input("Ingrese otro numero: "))
    count += 1

print("La suma de los números ingresados es:", suma ,"y el promedio es",(suma/count))

