suma = 0
contador = 0 
i = 1
while i <= 7:
  numero = int(input(f"Ingresa el número {i}: "))
  if numero % 2 == 0:
    suma += numero
    contador += 1
  i += 1
promedio = suma / contador
print(f"El promedio de los pares es: {promedio}")