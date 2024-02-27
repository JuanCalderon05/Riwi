contador = 0
i = 1
while i <= 7:
  numero = int(input(f"Ingresa el número {i}: "))
  if numero % 3 == 0:
    contador += 1
  i += 1  
print(f"Hay {contador} números divisibles por 3")