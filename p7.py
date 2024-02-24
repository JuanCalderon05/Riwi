num_ect = int(input("ingrese el numero de hectarias: "))

if num_ect < 100000:
  print("debes sembrar 10% de pino, 30% de cedro, 10% de arboles medicinales y el resto en plantas variadas")
elif num_ect >= 1000000  and num_ect <=2000000:
    print("debes sembrar 15% de pino, 35% de cedro, 20% de arboles medicinales y el resto en plantas variadas")
else:
   print("debes sembrar 20% de pino, 39% de cedro, 35% de arboles medicinales y el resto en plantas variadas")
  