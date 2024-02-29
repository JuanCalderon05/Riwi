capital_ = float(input("ingrese por favor el capital: "))
t_int = float(input("ingrese por favor la tasa de interes: "))
t_ = int(input("ingrese por favor el tiempo (meses): "))

Interes = capital_ * t_int * t_
V_Final = (1 + Interes * t_)*capital_

print(f"El interes simple de tu inversion es: {Interes} ")
print(f"El valor final de tu inversion es: {V_Final} ")