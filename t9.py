n = int(input("Ingresa un número: "))
suma = 0
i = 1
while i <= n:
  if i % 2 == 0:
    suma += i
  i += 1
print(f"La suma de los pares es: {suma}")