contador = 0
i = 1 
while i <= 10:
  numero = int(input("Ingresa un número: "))
  if numero % 2 == 0:
    contador += 1
  i += 1
print(f"Hay {contador} números pares")
