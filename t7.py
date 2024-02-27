contador = 0
i = 1
while i <= 10:
  numero = int(input("Ingresa un número entero: "))
  if numero > 100:
    contador += 1
  i += 1
print(f"Hay {contador} números mayores a 100")