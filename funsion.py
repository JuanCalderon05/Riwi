n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

def sum_(n1,n2):
    sum = n1+n2
    return sum

def rest_(n1,n2):
    rest = n1-n2
    return rest

def mul_(n1,n2):
    mul = n1*n2
    return mul

def div_(n1,n2):
    div = n1/n2
    return div

def mod_(n1,n2):
    mod = n1%n2
    return mod

print("1. Suma: ")
print("2. Resta: ")
print("3. Multiplicacion: ")
print("4. Divicion: ")
print("5. Modulo: ")
print("6. Modulo: ")
select = input(print("porfavor seleccione que operacion decea hacer: "))

while select == 1:
    suma = sum_(n1,n2)
    print("La suma es :" + suma)
