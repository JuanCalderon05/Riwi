
frase = input("\n\nIngrese una frase: ").lower()

a = []
e = []
i = []
o = []
u = []

for letra in frase:
    if letra == 'a':
        a.append(letra)
    elif letra == 'e':
        e.append(letra)
    elif letra == 'i':
        i.append(letra)
    elif letra == 'o':
        o.append(letra)
    elif letra == 'u':
        u.append(letra)

vocales = {'a': len(a), 'e': len(e), 'i': len(i), 'o': len(o), 'u': len(u)}

print("╔════════════════════════════════╗")
print("║    Cantidad de 'a':", len(a),"         ║ ")
print("╚════════════════════════════════╝")
print("╔════════════════════════════════╗")
print("║    Cantidad de 'e':", len(e),"         ║ ")
print("╚════════════════════════════════╝")
print("╔════════════════════════════════╗")
print("║    Cantidad de 'i':", len(i),"         ║ ")
print("╚════════════════════════════════╝")
print("╔════════════════════════════════╗")
print("║    Cantidad de 'o':", len(o),"         ║ ")
print("╚════════════════════════════════╝")
print("╔════════════════════════════════╗")
print("║    Cantidad de 'u':", len(u),"         ║ ")
print("╚════════════════════════════════╝")

vocal_mas_repetida = max(vocales, key=vocales.get)
vocal_menos_repetida = min(vocales, key=vocales.get)

print("╔════════════════════════════════════╗")
print("║ La vocal que más se repite es:", vocal_mas_repetida,"  ║ ")
print("╚════════════════════════════════════╝")
print("╔════════════════════════════════════╗")
print("║ La vocal que menos se repite es:", vocal_menos_repetida,"║ ")
print("╚════════════════════════════════════╝")