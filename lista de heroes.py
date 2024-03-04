superman_dict = {
    "Nombre": "Superman",
    "Edad": 32,
    "poderes": ["Super Fuerza", "Invulnerabilidad", "Vuelo", "Super Velocidad", "Visión Rayos X"],
    "Pareja": "Lois Lane"
}

batman_dict = {
    "Nombre": "Batman",
    "Edad": 30,
    "poderes": ["Dinero"],
    "Pareja": "Soltero"
}

mujer_maravilla_dict = {
    "Nombre": "Mujer Maravilla",
    "Edad": 30,
    "poderes": ["Super Fuerza", "Invulnerabilidad", "Magia"],
    "Pareja": "Ninguno"
}

heroes_list = [superman_dict, batman_dict, mujer_maravilla_dict]

def mostrar_datos(superheroes):
    for key, value in superheroes.items():
        print(f"{key}: {value}")
    print()

for heroes in heroes_list:
    mostrar_datos(heroes)

