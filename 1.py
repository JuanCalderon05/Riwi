import os

def clear_console():
    if os.name == 'posix':
        os.system('clear')

venta = []

while True:
    clear_console()
    val_ = float(input("POR FAVOR INGRESE EL VALOR DE VENTA: "))
    venta.append(val_)

    o_t = input("\nQuieres ingresar otro gasto? (s/n) \n") 
    if o_t.lower() != 's':
        break

prom_ = sum(venta) / len(venta)
min_ = min(venta)
max_ = max(venta)

print(f"EL PROMEDIO DE LAS VENTAS ES: {prom_} ")
print(f"EL MAXIMO DE LAS VENTAS ES: {max_} ")
print(f"EL MINIMO DE LAS VENTAS ES: {min_} ")
