nom_ = str(input("ingrese su nombre: "))
not_1 = float(input("nota de examen 1: "))
not_2 = float(input("nota de examen 2: "))
not_3 = float(input("nota de examen 3: "))
prom = (not_1+not_2+not_3)/3

if prom >=3 and prom <6:
  print(f"Sr.{nom_}, Aprobaste la materia")
elif prom <3:
  print(f"Sr.{nom_}, Reprobaste la materia")
  