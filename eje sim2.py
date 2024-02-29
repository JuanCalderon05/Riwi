import os

def clear_console():
    if os.name == 'posix':
        os.system('clear')

valor_final = []

while True:
    clear_console()
    capital_inicial = float(input("Ingrese el capital inicial:"))
    plazo = int(input("Ingrese el plazo (años): "))
    
    if 1 <= plazo <= 2:
        tasa_interes = 0.07
    elif 2 < plazo <= 5:
        tasa_interes = 0.10
    else:
        tasa_interes = 0.15
    
    V_Final = (1 + tasa_interes * plazo) * capital_inicial
    
    valor_final.append(V_Final)

    o_t = input("\n¿Quieres ingresar otro CDT? (s/n)\n") 
    if o_t.lower() != 's':
        break

suma_v_f = sum(valor_final)

print(f"El capital total de los CDT de los usuarios es: {suma_v_f}")
