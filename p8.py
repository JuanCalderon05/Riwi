num_pc = int(input("por favor ingrese el numero de computadore que vas a comprar_: "))
if num_pc < 5 and num_pc > 0:
  print("recibiste el 10 % de descuento sobre el total de la compra")
elif num_pc == 0:
  print("digite un numero correcto")
elif num_pc >= 5 and num_pc < 10:
  print("recibiste un 20% de descuento")
elif num_pc > 10:
  print("recibiste el 40% de descuento")