ali = []
trans = []
viv = []
entre = []

salario = int(input("por favor ingrese su salario: "))
while True:
    gasto = int(input("por favor ingrese su gasto: "))


    print("\nCATEGORIAS:\n")
    print("1.\t  ALIMENTOS  \t")
    print("2.\t  TRANSPORTE  \t")
    print("3.\t  VIVENDA  \t")
    print("4.\t  ENTRETENIMIENTO  \t")
    print("5.\t  SALIR  \t")
    
    select = int(input("POR FAVOR SELECCIONE UNA CATEGORIA A LA CUAL DESEA AGG EL GASTO: "))
    
    if select == 5: 
      break
    
    if select == 1: 
      ali.append(gasto)
    
    if select == 2: 
      ali.append(gasto)
    
    if select == 3: 
      viv.append(gasto)
    
    if select == 4: 
      entre.append(gasto)
      
sum = salario - (sum(ali)+sum(trans)+sum(viv)+sum(entre))
print(f"Su saldo restante es{sum}")
