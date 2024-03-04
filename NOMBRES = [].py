
nombres = []
APOSITIVO = []
ANEGATIVO = []
BPOSITIVO = []
BNEGATIVO = []
OPOSITIVO = []
ONEGATIVO = []
AB_pos = []
AB_neg = []

while True:

    name = input("Ingrese su nombre completo: ")
    nombres.append(name)
    rh = input("Ingrese su RH (EN MAYUSCULAS): ")
    if rh in ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']:
        if rh == 'O+':
            OPOSITIVO.append(rh)
        elif rh == 'O-':
            ONEGATIVO.append(rh)
        elif rh == 'A+':
            APOSITIVO.append(rh)
        elif rh == 'A-':
            ANEGATIVO.append(rh)
        elif rh == 'B+':
            BPOSITIVO.append(rh)
        elif rh == 'B-':
            BNEGATIVO.append(rh)
        elif rh == 'AB+':
            AB_pos.append(rh)
        elif rh == 'AB-':
            AB_neg.append(rh)
        continue_input = input("\nDesea ingresar otro dato? s/n ").lower()
        if continue_input != 's':
            break
    else:
        print("RH invalido, ingrese nuevamente")

print("\t\nCANTIDAD DE PACIENTES POR RH\n")
print("O positivo: ", len(OPOSITIVO))
print("O negativo: ", len(ONEGATIVO))
print("A positivo: ", len(APOSITIVO))
print("A negativo: ", len(ANEGATIVO))
print("B positivo: ", len(BPOSITIVO))
print("B negativo: ", len(BNEGATIVO))
print("AB positivo: ", len(AB_pos))
print("AB negativo: ", len(AB_neg))

lentotal = len(OPOSITIVO)+len(ONEGATIVO)+len(APOSITIVO)+len(ANEGATIVO)+len(BPOSITIVO)+len(BNEGATIVO)+len(AB_pos)+len(AB_neg)

print("\t\nPORCENTAJE DE LA CANTIDAD DE PACIENTES POR RH\n")
print("O positivo: ", (len(OPOSITIVO)/lentotal)*100,"%")
print("O negativo: ", (len(ONEGATIVO)/lentotal)*100,"%")
print("A positivo: ", (len(APOSITIVO)/lentotal)*100,"%")
print("A negativo: ", (len(ANEGATIVO)/lentotal)*100,"%")
print("B positivo: ", (len(BPOSITIVO)/lentotal)*100,"%")
print("B negativo: ", (len(BNEGATIVO)/lentotal)*100,"%")
print("AB positivo: ", (len(AB_pos)/lentotal)*100,"%")
print("AB negativo: ", (len(AB_neg)/lentotal)*100,"%")


.0