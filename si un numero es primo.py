def es_primo():
    num =  int(input("Ingrese un numero: "))
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True

es_primo()