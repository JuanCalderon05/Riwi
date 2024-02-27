suma = 0
i = 1
while i <= 5:
  altura = float(input(f"Ingresa la altura {i} (en metros): "))
  suma += altura 
  i += 1
promedio = suma / 5
print(f"El promedio de las alturas es: {promedio}")