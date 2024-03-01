import random
import os

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

laberinto = [
    ["encrucijada","criatura"],
    ["pasillo","sorpresa"],
    ["pasillo","llave"],
    ["pasillo","criatura"],
    ["encrucijada","sorpresa"],   
]

random.shuffle(laberinto)

def jugar_nuevo():
    random.shuffle(laberinto)

    posicion_actual = 1

    while True:

        clear_console()

        print("╔════════════════════════════════╗")
        print("║           LABERINTO            ║")
        print("╚════════════════════════════════╝")
        print(f"Estás en {laberinto[posicion_actual][0]}.")
        print("══════════════════════════════════")

        if posicion_actual < 1:
            print("Puedes ir a la Derecha.")

        elif posicion_actual > 3:
            print("Puedes ir a la Izquierda.")

        else:
            print("Puedes ir a la Izquierda o a la Derecha.")
        print("══════════════════════════════════")
        
        select = input("¿Qué quieres hacer? (I/D): ").upper()
        
        if select == 'I' and posicion_actual > 0:
            posicion_actual -= 1

        elif select == 'D' and posicion_actual < 4:
            posicion_actual += 1

        else:
            print("VUELVE A INTENTARLO.")

        if laberinto[posicion_actual][1] == "criatura":
            print("══════════════════════════════════")
            print("¡Has encontrado una criatura!")
            print("══════════════════════════════════")

            jugar_de_nuevo = input("¿Quieres volver a jugar? (s/n): ").lower()

            if jugar_de_nuevo == 's':
                jugar_nuevo()
            else:
                print("Gracias por jugar.")
                break

        elif laberinto[posicion_actual][1] == "llave":
            print("══════════════════════════════════")
            print("FELICIDADES, HAS ESCAPADO DEL LABERINTO.")
            print("══════════════════════════════════")
            break
        
jugar_nuevo()