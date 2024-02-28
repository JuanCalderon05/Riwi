import os

def clear_console():
    if os.name == 'posix':
        os.system('clear')

def es_num (num):
  try:
    return int(num)
  except:
    return False
def suma( n1 , n2 ):
  sum = n1 + n2
  return sum
def resta( n1 , n2 ):
  rest = n1 - n2
  return rest
def multiplicacion( n1 , n2 ):
  mult = n1 * n2
  return mult
def division( n1 , n2 ):
  if n2 == 0:
    return " \nno se puede dividir"
  else:
    div = n1 / n2
    return div
def modulo( n1 , n2 ):
  mod = n1 % n2
  return mod

while True:
    clear_console()
    print("\nINGRESE POR FAVOR DOS NUMEROS A LA CALCULADORA\n")


    n1= int(input("por favor ingrese el primer numero: "))
    n2= int(input("\npor favor ingrese el segundo numero: "))
    
    print("\nOPCIONES:\n")
    print(" 1.\t  SUMA")
    print(" 2.\t  RESTA")
    print(" 3.\t  MULTIPLICACION")
    print(" 4.\t  DIVISION")
    print(" 5.\t  MODULO")
    print(" 6.\t  SALIR\n")

    select = es_num(input("\nPOR FAVOR SELECCIONE UNA DE LAS OPCIONES: "))
    if select == 6:
      break
    if select == 1:
      su_ = suma(n1 , n2)
      print("\n",su_)
    if select == 2:
      re_ = resta(n1 , n2)
      print("\n",re_)
    if select == 3:
      mu_ = multiplicacion(n1 , n2)
      print("\n",mu_)
    if select == 4:
      di_ = division(n1 , n2)
      print("\n",di_)
    if select == 5:
      mo_ = modulo(n1 , n2)
      print("\n",mo_)  
    if select == False:
      print("ingresa un dato valido")
      
    o_t = input("\nQuiere hacer otra operacion (s/n): \n") 
    if o_t.lower != 's':
      break
    
