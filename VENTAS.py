ventas = [725, 383, 420, 645, 932]

total_semanal = sum(ventas)

promedio_diario = total_semanal / len(ventas)

dia_max = ventas.index(max(ventas))
venta_max = max(ventas)

dia_min = ventas.index(min(ventas))
venta_min = min(ventas)

dias_por_debajo = [dia for dia, venta in enumerate(ventas) if venta < promedio_diario]

print("Promedio de ventas por día:", promedio_diario)
print("Día con la venta más alta:", dia_max + 1, "(Venta:", venta_max, "UN)")
print("Día con la venta más baja:", dia_min + 1, "(Venta:", venta_min, "UN)")
print("Días por debajo del promedio de ventas:", [dia + 1 for dia in dias_por_debajo])