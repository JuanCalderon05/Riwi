num = int(input('Ingrese un número entero positivo menor a 327768: '))

if num < 0 or num >= 327768:
    print('Número incorrecto') 

elif num % 4 == 0:
    print(num / 4)

elif num % 5 == 0:
    print((num / 5) ** 2)
    
elif num % 7 == 0:
    print((num / 8))
else:
    print('Número extraño')