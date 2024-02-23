num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

if num1 <= num2 and num1 <= num3:
    menor = num1  
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3  
medio = (num1 + num2 + num3) - mayor - menor

print(f"Los números en orden decreciente son: {mayor}, {medio}, {menor}")