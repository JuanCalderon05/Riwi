num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = 0
for i in range(num2):
    resultado += num1
if num1 < 0 and num2 < 0:
    resultado = resultado
print("El resultado de la multiplicación es:", resultado)
