numero = int(input("Ingrese un número: "))
count = 0
print("Los divisores exactos de", numero, "son:")
for i in range(numero + 1):
    if i != 0 and numero % i == 0:
        count += 1
        print(i)
print("la cantidad de divisores de dicho numero es: ",count)