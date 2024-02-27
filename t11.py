contador = 0
i = 1
while i <= 7:
  numero = int(input(f"Ingresa el número {i}: "))
  if numero % 5 == 0:
    contador += 1
  i += 1
print(f"Hay {contador} múltiplos de 5")