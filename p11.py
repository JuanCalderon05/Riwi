print("¡Bienvenido al juego de preguntas de sí o no!")
print("Responde correctamente las 3 preguntas para ganar.")

pregunta1 = input("¿Colón descubrió América? (sí/no): ").lower()
pregunta2 = input("¿La independencia de Colombia fue en 1810? (sí/no): ").lower()
pregunta3 = input("¿Tokio es un país? (sí/no): ").lower()

respuestas_correctas = 0

if pregunta1 == "no":
    respuestas_correctas += 1
    print("¡Respuesta correcta!")
else:
    print("Respuesta incorrecta.")

if pregunta2 == "si":
    respuestas_correctas += 1
    print("¡Respuesta correcta!")
else:
    print("Respuesta incorrecta.")

if pregunta3 == "no":
    respuestas_correctas += 1
    print("¡Respuesta correcta!")
else:
    print("Respuesta incorrecta.")

if respuestas_correctas == 3:
    print("¡Felicidades! Has ganado el juego.")
else:
    print(f"Lo siento, has respondido correctamente {respuestas_correctas} preguntas. ¡Sigue intentando!")