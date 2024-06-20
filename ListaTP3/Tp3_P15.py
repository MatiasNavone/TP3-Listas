entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120,
        "pokemones": [
            {"nombre": "Pikachu", "nivel": 80, "tipo": "Eléctrico", "subtipo": None},
            {"nombre": "Bulbasaur", "nivel": 65,
                "tipo": "Planta", "subtipo": "Veneno"},
            {"nombre": "Squirtle", "nivel": 60, "tipo": "Agua", "subtipo": None},
            {"nombre": "Greninja", "nivel": 90,
                "tipo": "Agua", "subtipo": "Siniestro"}
        ]
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40,
        "pokemones": [
            {"nombre": "Cinderace", "nivel": 75, "tipo": "Fuego", "subtipo": None},
            {"nombre": "Flygon", "nivel": 70, "tipo": "Tierra", "subtipo": "Dragón"},
            {"nombre": "Golurk", "nivel": 65,
                "tipo": "Tierra", "subtipo": "Fantasma"},
            {"nombre": "Sobble", "nivel": 50, "tipo": "Agua", "subtipo": None},
            {"nombre": "Scyther", "nivel": 60, "tipo": "Bicho", "subtipo": "Volador"}
        ]
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100,
        "pokemones": [
            {"nombre": "Charizard", "nivel": 100,
                "tipo": "Fuego", "subtipo": "Volador"},
            {"nombre": "Rillaboom", "nivel": 85,
                "tipo": "Planta", "subtipo": None},
            {"nombre": "Haxorus", "nivel": 88, "tipo": "Dragón", "subtipo": None}
        ]
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30,
        "pokemones": [
            {"nombre": "Eevee", "nivel": 45, "tipo": "Normal", "subtipo": None},
            {"nombre": "Espeon", "nivel": 55, "tipo": "Psíquico", "subtipo": None}
        ]
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60,
        "pokemones": [
            {"nombre": "Duraludon", "nivel": 85,
                "tipo": "Acero", "subtipo": "Dragón"},
            {"nombre": "Flygon", "nivel": 80, "tipo": "Tierra", "subtipo": "Dragón"},
            {"nombre": "Garchomp", "nivel": 85,
                "tipo": "Dragón", "subtipo": "Tierra"},
            {"nombre": "Togekiss", "nivel": 75,
                "tipo": "Hada", "subtipo": "Volador"},
            {"nombre": "Tyranitar", "nivel": 82,
                "tipo": "Roca", "subtipo": "Siniestro"}]
    }
]


print("")
print("Punto A")

def cantidad_pokemones():
    cantidad_pokemon = 0
    for entrenador in entrenadores:
        if 'pokemones' in entrenador:
            for pokemon in entrenador['pokemones']:
                cantidad_pokemon += 1
            print("El entrenador ",
                  entrenador['nombre'], "tiene", cantidad_pokemon, "pokemones")
            cantidad_pokemon = 0


cantidad_pokemones()

print(" ")


print("")
print("Punto B")


def torneos_ganados():
    ganadores_torneo = []
    for entrenador in entrenadores:
        if entrenador['torneos_ganados'] > 3:
            ganadores_torneo.append(entrenador['nombre'])
    return ganadores_torneo


ganadores = torneos_ganados()
print(ganadores)

print(" ")

print("")
print("Punto C")


def pokemon_mayor_niv():
    mayor_entrenador = 0
    nombre_mayor = 0
    nombre_pokemon = 0
    pokemon_mayor = 0

    for entrenador in entrenadores:
        if entrenador['torneos_ganados'] > mayor_entrenador:
            nombre_mayor = entrenador['nombre']
            mayor_entrenador = entrenador['torneos_ganados']
            for pokemon in entrenador['pokemones']:
                if pokemon['nivel'] > pokemon_mayor:
                    nombre_pokemon = pokemon['nombre']
                    pokemon_mayor = pokemon['nivel']
    print("Pokemon", nombre_pokemon, "Nivel", pokemon_mayor,
          "Entrenador", nombre_mayor, "Torneos Ganados", mayor_entrenador)


pokemon_mayor_niv()

print(" ")

print("")
print("Punto D")


def info_entrenador():
    entrenador_info = {}
    for entrenador in entrenadores:
        if entrenador['nombre'] == 'Ash Ketchum':
            entrenador_info['nombre'] = entrenador["nombre"]
            entrenador_info['torneos ganados'] = entrenador["torneos_ganados"]
            entrenador_info['batallas ganadas'] = entrenador["batallas_ganadas"]
            entrenador_info['batallas perdidas'] = entrenador["batallas_perdidas"]
    return entrenador_info


def informacion_pokemon():
    pokemones_info = []
    for entrenador in entrenadores:
        if entrenador['nombre'] == 'Ash Ketchum':
            for pokemon in entrenador["pokemones"]:
                pokemon_info = {
                    'nombre': pokemon["nombre"],
                    'nivel': pokemon["nivel"],
                    'tipo': pokemon["tipo"],
                    'subtipo': pokemon["subtipo"]
                }
                pokemones_info.append(pokemon_info)
    return pokemones_info


b = info_entrenador()
print(b)

a = informacion_pokemon()
print(a)

print(" ")


print("")
print("Punto E")


def porcen_ganadas():
    porcentaje = []
    for entrenador in entrenadores:
        batallas_totales = entrenador['batallas_ganadas'] + \
            entrenador['batallas_perdidas']
        if batallas_totales > 0:
            porcentaje_ganadas = (
                entrenador['batallas_ganadas'] / batallas_totales) * 100
            if porcentaje_ganadas > 79:
                porcentaje.append(entrenador['nombre'])
    return porcentaje


entrenadores_alto_porcentaje = porcen_ganadas()
print(entrenadores_alto_porcentaje)

print(" ")


print("")
print("Punto F")


def tipo_pokemones():
    pokemones_tipo = []
    for entrenador in entrenadores:
        tiene_fuego = False
        tiene_planta = False
        tiene_agua = False
        tiene_volador = False
        for pokemon in entrenador['pokemones']:
            if pokemon['tipo'] == 'Fuego' or pokemon['subtipo'] == 'Fuego':
                tiene_fuego = True
            if pokemon['tipo'] == 'Planta' or pokemon['subtipo'] == 'Planta':
                tiene_planta = True
            if pokemon['tipo'] == 'Agua' or pokemon['subtipo'] == 'Agua':
                tiene_agua = True
            if pokemon['tipo'] == 'Volador' or pokemon['subtipo'] == 'Volador':
                tiene_volador = True

        if (tiene_fuego and tiene_planta) or (tiene_agua and tiene_volador):
            pokemones_tipo.append(entrenador['nombre'])
    return pokemones_tipo


TiposPokemones = tipo_pokemones()
print("Los entrenadores con tipo fuego/planta o agua/volador son", TiposPokemones)

print(" ")


print("")
print("Punto G")


def nivel_total():
    niveles_totales_pokemon = 0
    for entrenador in entrenadores:
        if entrenador['nombre'] == 'Ash Ketchum':
            for pokemon in entrenador["pokemones"]:
                niveles_totales_pokemon += pokemon['nivel']
    return niveles_totales_pokemon


tot_nivel = nivel_total()


def pokemones_ash():
    cantidad_pokemon = 0
    for entrenador in entrenadores:
        if entrenador['nombre'] == 'Ash Ketchum':
            for pokemon in entrenador['pokemones']:
                cantidad_pokemon += 1
    return cantidad_pokemon


pokemon_cantidad = pokemones_ash()


promedio_niveles = tot_nivel / pokemon_cantidad
print(f"Promedio total de niveles en Ash Ketchum: {promedio_niveles}")


print(" ")


print("")
print("Punto H")


def encontrar_pikachu():
    Entrenador_Con_Pikachu = []
    for entrenador in entrenadores:
        for pokemon in entrenador['pokemones']:
            if pokemon['nombre'] == 'Pikachu':
                Entrenador_Con_Pikachu.append(entrenador['nombre'])
    return Entrenador_Con_Pikachu


Pikachu = encontrar_pikachu()
print(f"El entrenador de Pikachu es:  {Pikachu}")

print(" ")

print("")
print("Punto I")



def pokemones_repetidos():
    pokemones = []
    for entrenador in entrenadores:
        pokemones_vistos = []
        tiene_repetidos = False
        for pokemon in entrenador['pokemones']:
            if pokemon['nombre'] in pokemones_vistos:
                tiene_repetidos = True
                break
            else:
                pokemones_vistos.append(pokemon['nombre'])
        if tiene_repetidos:
            pokemones.append(entrenador['nombre'])
    return pokemones


entrenadores_con_pokemon_repetido = pokemones_repetidos()
if len(entrenadores_con_pokemon_repetido) > 0:
    print("los siguientes entrenadores tienen pokemones repetidos:")
    for nombre_entrenador in entrenadores_con_pokemon_repetido:
        print(nombre_entrenador)
else:
    print("ningun entrenador tiene pokemones repetidos.")

print(" ")



print("")
print("Punto J")


def encontrar_pokemon():
    buscar = {"Tyrantrum", "Terrakion", "Wingull"}
    entrenadores_especificos = []
    for entrenador in entrenadores:
        if 'pokemones' in entrenador:
            for pokemon in entrenador['pokemones']:
                if pokemon['nombre'] in buscar:
                    entrenadores_especificos.append(entrenador['nombre'])


entrenadores_especificos = encontrar_pokemon()
print("Los entrenadores con Tyrantrum, Terrakion o Wingull son:",
      entrenadores_especificos)


print(" ")


print("")
print("Punto K")

nombre_entrenador = input("Ingresa el nombre del entrenador: ")
nombre_pokemon = input("Ingresa el nombre del pokemon: ")


def ingresar():
    inf_entrenador = []
    for entrenador in entrenadores:
        if entrenador['nombre'] == nombre_entrenador:
            for pokemon in entrenador['pokemones']:
                if pokemon['nombre'] == nombre_pokemon:
                    inf_entrenador.append(entrenador['nombre'])
                    inf_entrenador.append(entrenador['torneos_ganados'])
                    inf_entrenador.append(entrenador['batallas_ganadas'])
                    inf_entrenador.append(entrenador['batallas_perdidas'])
            return pokemon, inf_entrenador
    return None, None


entrenador_encontrado, pokemon_encontrado = ingresar()

if entrenador_encontrado is not None and pokemon_encontrado is not None:
    print("Entrenador encontrado:", entrenador_encontrado)
    print("Pokemon encontrado:", pokemon_encontrado)
else:
    print("El entrenador no tiene ese pokemon.")

print(" ")