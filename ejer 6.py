hombres = 0
mujeres = 0
total_personas = 0
while True:
    genero = input("Ingrese el género de la persona (H para hombre, M para mujer): ").upper()
    if genero == 'H':
        hombres += 1
    elif genero == 'M':
        mujeres += 1
    else:
        print("Entrada inválida. Por favor, ingrese 'H' para hombre o 'M' para mujer.")
        continue
    total_personas += 1
    otro_dato = input("¿Desea ingresar otro dato? (Sí/No): ").lower()
    if otro_dato != 'si':
        break
porcentaje_hombres = (hombres / total_personas) * 100
porcentaje_mujeres = (mujeres / total_personas) * 100
print("Número total de hombres:", hombres)
print("Número total de mujeres:", mujeres)
print("Porcentaje de hombres:", porcentaje_hombres, "%")
print("Porcentaje de mujeres:", porcentaje_mujeres, "%")

