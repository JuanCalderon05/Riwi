clase_cliente = input("Ingrese la clase de cliente (mayorista, minoritario, ocasional): ")
antiguedad = int(input("Ingrese la antigüedad del cliente (en años): "))

if clase_cliente == "mayorista":
    if antiguedad > 2:
        descuento = 0.25
    elif antiguedad <= 2:
        descuento = 0.2
    else:
        descuento = 0

elif clase_cliente == "minoritario":
    if antiguedad > 5:
        descuento = 0.18
    else:
        descuento = 0

elif clase_cliente == "ocasional":
    descuento = 0.1

else:
    descuento = 0

valor_compra = float(input("Ingrese el valor de la compra sin descuento: "))
valor_a_pagar = valor_compra * (1 - descuento)
print(f"El valor a pagar con descuento es: ${valor_a_pagar:.2f}")