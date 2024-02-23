import random

total_compra = float(input("Introduce el total de la compra: "))

numero = random.randint(1, 100) 

if numero < 74:
    descuento = total_compra * 0.15
else:
    descuento = total_compra * 0.2

print(f"El número aleatorio es: {numero}")  
print(f"El descuento es de: {descuento:.2f}")

total_pagar = total_compra - descuento
print(f"El total a pagar es: {total_pagar:.2f}")