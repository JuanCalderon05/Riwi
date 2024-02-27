suma = 0
i = 1
while i <= 10:
  numero = int(input("Ingresa un número: "))
  if numero < 0:
    suma += numero
  i += 1
print(f"La suma de los negativos es: {suma}")