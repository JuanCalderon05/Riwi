print("¡Bienvenido al juego 'Tibio, Caliente o Frío'!")
print("Cada jugador tiene tres intentos para adivinar el número secreto.")
print("El juego proporciona pistas al jugador:")
print("Caliente si el intento está dentro de tres números del número secreto")
print("Tibio si el intento está entre tres y cinco números de distancia del número secreto")
print("Frío en cualquier otro caso")

def registrar_jugador():
    nombre = input("Ingresa tu nombre: ")
    return nombre

def generar_numero_secreto():
    return 9

def obtener_num():
    suposicion = int(input("Ingresa tu numero: "))
    return suposicion

def verificar_num(numero_secreto, suposicion):
    if abs(numero_secreto - suposicion) <= 3:
        return "Caliente"
    elif abs(numero_secreto - suposicion) <= 5:
        return "Tibio"
    else:
        return "Frío"
def jugar(jugador):
    numero_secreto = generar_numero_secreto()
    intentos = 0
    for _ in range(3):
        suposicion = obtener_num()
        resultado = verificar_num(numero_secreto, suposicion)

        intentos += 1
        if suposicion == numero_secreto:
            print(f"{jugador}, ¡felicidades! Has adivinado el número secreto: {numero_secreto}")
            return resultado, intentos

        print(f"{jugador}, tu suposición es {resultado}")
    print(f"{jugador}, no has adivinado el número secreto. El número secreto era: {numero_secreto}")
    return resultado, intentos

jugadores = {}
while True:
    nombre_jugador = registrar_jugador()
    if nombre_jugador.lower() == "q":
        break
    jugadores[nombre_jugador] = jugar(nombre_jugador)

resultados = {}
intentos_totales = {}
for jugador, (resultado, intentos) in jugadores.items():
    if resultado not in resultados:
        resultados[resultado] = 0
        intentos_totales[resultado] = 0
    resultados[resultado] += 1
    intentos_totales[resultado] += intentos

total_jugadores = sum(intentos_totales.values())
print("\nResultados del juego:")
for resultado, cantidad in resultados.items():
    porcentaje = (cantidad / total_jugadores) * 100
    print(f"- {resultado}: {porcentaje:.2f}%")