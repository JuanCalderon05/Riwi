suma = 0
numero = int(input("Ingresa un número positivo (negativo para terminar): "))
while numero >= 0:
  suma += numero
  numero = int(input("Ingresa un número positivo (negativo para terminar): "))
print(f"La suma es: {suma}")