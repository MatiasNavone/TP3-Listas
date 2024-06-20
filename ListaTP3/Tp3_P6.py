superheroes = [
    {"nombre": "Linterna Verde", "anio_aparicion": 1940, "casa": "DC", "biografia": "Usa un anillo de poder."},
    {"nombre": "Wolverine", "anio_aparicion": 1974, "casa": "Marvel", "biografia": "Tiene garras de adamantium."},
    {"nombre": "Dr. Strange", "anio_aparicion": 1963, "casa": "DC", "biografia": "Es un maestro de las artes místicas."},
    {"nombre": "Capitana Marvel", "anio_aparicion": 1968, "casa": "Marvel", "biografia": "Tiene poderes cósmicos."},
    {"nombre": "Mujer Maravilla", "anio_aparicion": 1941, "casa": "DC", "biografia": "Es una amazona con superpoderes."},
    {"nombre": "Flash", "anio_aparicion": 1940, "casa": "DC", "biografia": "El hombre más rápido del mundo."},
    {"nombre": "Star-Lord", "anio_aparicion": 1976, "casa": "Marvel", "biografia": "Líder de los Guardianes de la Galaxia."},
    {"nombre": "Batman", "anio_aparicion": 1939, "casa": "DC", "biografia": "El caballero de la noche, usa un traje de murciélago."},
    {"nombre": "Superman", "anio_aparicion": 1938, "casa": "DC", "biografia": "El hombre de acero, tiene una armadura kryptoniana."},
    {"nombre": "Spiderman", "anio_aparicion": 1962, "casa": "Marvel", "biografia": "El trepamuros de Nueva York."},
]
print("")
print("Punto A")
def eliminar_superheroe(superheroes, nombre):
    for i, heroe in enumerate(superheroes):
        if heroe["nombre"] == nombre:
            del superheroes[i]
            break

eliminar_superheroe(superheroes, "Linterna Verde")

print("")
print("Punto B")

def anio_aparicion(superheroes, nombre):
    for heroe in superheroes:
        if heroe["nombre"] == nombre:
            return heroe["anio_aparicion"]

print(f"año de aparición de Wolverine: {anio_aparicion(superheroes, 'Wolverine')}")

print("")
print("Punto C")

def cambiar_casa(superheroes, nombre, nueva_casa):
    for heroe in superheroes:
        if heroe["nombre"] == nombre:
            heroe["casa"] = nueva_casa

cambiar_casa(superheroes, "Dr. Strange", "Marvel")

print("")
print("Punto D")

def traje_armadura(superheroes):
    resultado = []
    for heroe in superheroes:
        if "traje" in heroe["biografia"] or "armadura" in heroe["biografia"]:
            resultado.append(heroe["nombre"])
    return resultado

print(f"Superhéroes que mencionan 'traje' o 'armadura': {traje_armadura(superheroes)}")

print("")
print("Punto E")

def anterior_1963(superheroes):
    resultado = []
    for heroe in superheroes:
        if heroe["anio_aparicion"] < 1963:
            resultado.append((heroe["nombre"], heroe["casa"]))
    return resultado

print(f"Superhéroes anteriores a 1963: {anterior_1963(superheroes)}")

print("")
print("Punto F")

def casa_superheroe(superheroes, nombre):
    for heroe in superheroes:
        if heroe["nombre"] == nombre:
            return heroe["casa"]

print(f"Casa de Capitana Marvel: {casa_superheroe(superheroes, 'Capitana Marvel')}")
print(f"Casa de Mujer Maravilla: {casa_superheroe(superheroes, 'Mujer Maravilla')}")

print("")
print("Punto G")

def info_superheroe(superheroes, nombres):
    resultado = []
    for heroe in superheroes:
        if heroe["nombre"] in nombres:
            resultado.append(heroe)
    return resultado

informacion = info_superheroe(superheroes, ["Flash", "Star-Lord"])
for info in informacion:
    print(info)

print("")
print("Punto H")
def listar_x_letras(superheroes, letras):
    resultado = []
    for heroe in superheroes:
        if heroe["nombre"][0] in letras:
            resultado.append(heroe["nombre"])
    return resultado

print(f"Superhéroes que comienzan con B, M o S: {listar_x_letras(superheroes, ['B', 'M', 'S'])}")

print("")
print("Punto I")
def contar_x_casa(superheroes):
    contador = {"Marvel": 0, "DC": 0}
    for heroe in superheroes:
        if heroe["casa"] in contador:
            contador[heroe["casa"]] += 1
    return contador

print(f"Cantidad de superhéroes por casa: {contar_x_casa(superheroes)}")

print("")
print("lista modificada")
print(superheroes)