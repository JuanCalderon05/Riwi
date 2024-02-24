
peso = 70

actividad = input("Ingrese la actividad (dormir/sentado): ")
tiempo = float(input("Ingrese el tiempo en minutos: "))

calorias_por_minuto = {"dormir": 1.28, "sentado": 1.73}

if actividad == "dormir":
    calorias_consumidas = calorias_por_minuto["dormir"] * tiempo
elif actividad == "sentado":
    calorias_consumidas = calorias_por_minuto["sentado"] * tiempo
else:
    calorias_consumidas = "Actividad no válida"

if isinstance(calorias_consumidas, float):
    total_calorias = calorias_consumidas * peso
    print("Calorías consumidas:", total_calorias)
else:
    print(calorias_consumidas)
