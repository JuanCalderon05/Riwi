import os

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


ali = []
trans = []
viv = []
entre = []

salario = int(input("Por favor ingrese su salario: "))

while True:
        clear_console()
        print("SU SALARIO ES: ",salario)
        gasto = int(input("Por favor ingrese su gasto: "))

        print("\nCATEGORÍAS:\n")
        print("1.\t ALIMENTOS  \t")
        print("2.\t TRANSPORTE  \t")
        print("3.\t VIVIENDA  \t")
        print("4.\t ENTRETENIMIENTO  \t")
        print("0.\t SALIR  \t")
        
        select = int(input("\nPOR FAVOR SELECCIONE UNA CATEGORÍA A LA CUAL DESEA AGREGAR EL GASTO: "))
        
        if select == 0: 
            break
        
        if select == 1: 
            ali.append(gasto)
        
        elif select == 2: 
            trans.append(gasto)
        
        elif select == 3: 
            viv.append(gasto)
        
        elif select == 4: 
            entre.append(gasto)

        o_t = input("\nQuieres ingresar otro gasto? (s/n) \n") 
        if o_t.lower() != 's':
            break

total_gastos = sum(ali) + sum(trans) + sum(viv) + sum(entre)
saldo_restante = salario - total_gastos

if saldo_restante < 0:
    print("\n¡ESTÁS GASTANDO MÁS DE LO QUE DEBERÍAS!")

print("*************************************************")

print("\tTOTAL DE GASTOS:           ",total_gastos)

print("\tSALDO RESTANTE:            ",saldo_restante)

print("\n\t\tGASTO POR CATEGORÍAS\t")

print("\tALIMENTOS:                 ",sum(ali))

print("\tTRANSPORTE:                ",sum(trans))

print("\tVIVIENDA:                  ",sum(viv))

print("\tENTRETENIMIENTO:           ",sum(entre))

print("*************************************************")
