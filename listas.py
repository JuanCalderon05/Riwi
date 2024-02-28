
edades = [41, 32, 75, 14, 28, 32, 81, 11, 24]

promedio_total = sum(edades) / len(edades)

sum_mayores_edad, count_mayores_edad, sum_menores_edad, count_menores_edad = 0, 0, 0, 0

for edad in edades:
    if edad >= 18:
        sum_mayores_edad += edad
        count_mayores_edad += 1
    else:
        sum_menores_edad += edad
        count_menores_edad += 1

promedio_mayores_edad = sum_mayores_edad / count_mayores_edad if count_mayores_edad else 0
promedio_menores_edad = sum_menores_edad / count_menores_edad if count_menores_edad else 0


arriba_promedio = sum(edad > promedio_total for edad in edades)
abajo_promedio = sum(edad < promedio_total for edad in edades)

print("1. Promedio de todas las edades:", promedio_total)
print("2. Promedio de las personas mayores de edad:", promedio_mayores_edad)
print("3. Promedio de las personas menores de edad:", promedio_menores_edad)
print("4. Edades por encima del promedio:", arriba_promedio)
print("5. Edades por debajo del promedio:", abajo_promedio)
