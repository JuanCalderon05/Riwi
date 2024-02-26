estra_ = int(input("Ingrese si estrato '1','2','3','4', ETC. : "))
sal_ = float(input("Ingrese su salario : "))
match(estra_):
    case 1:
        print("Hola, tu bono fue de",(sal_*0.35),"$ y tu salario sera: ", (sal_*0.35)+sal_,"$")
    case 2:
        print("Hola, tu bono fue de",(sal_*0.25),"$ y tu salario sera: ", (sal_*0.25)+sal_,"$")
    case 3:
        print("Hola, tu bono fue de",(sal_*0.2),"$ y tu salario sera: ", (sal_*0.20)+sal_,"$")
    case 4:
        print("Hola, tu bono fue de",(sal_*0.15),"$ y tu salario sera: ", (sal_*0.15)+sal_,"$")
    case 5:
        print("Hola, tu bono fue de",(sal_*0.10),"$ y tu salario sera: ", (sal_*0.10)+sal_,"$")
    case 6:
        print("Hola, tu bono fue de",(sal_*0.10),"$ y tu salario sera: ", (sal_*0.10)+sal_,"$")
    case _:
        print("Hola, digite los datos correctamente")