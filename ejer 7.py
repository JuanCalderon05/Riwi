suma_notas = 0
nota_maxima = float('-inf')
nota_minima = float('inf')

for i in range(5):
    nota = float(input("Ingrese la nota: "))
    suma_notas += nota
    if nota > nota_maxima:
        nota_maxima = nota   
    if nota < nota_minima:
        nota_minima = nota
promedio = suma_notas / 5
print("El promedio de las notas es:", promedio)
print("La nota más alta es:", nota_maxima)
print("La nota más baja es:", nota_minima)
