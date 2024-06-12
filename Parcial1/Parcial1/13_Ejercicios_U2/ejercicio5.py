# Crear una lista con el contenido de la tabla
tabla_contenido = [
    "-ACCIÓN",
    "MÁXIMA VELOCIDAD",
    "ARMA MORTAL 4",
    "RAPIDO Y FURIOSO 1",
    "-TERROR",
    "LA MONJA",
    "LA MALDICIÓN",
    "EL CONJURO",
    "-DEPORTES",
    "ESPN",
    "MÁS DEPORTE",
    "ACCIÓN DEPORTE"
]

# Crear un diccionario con el contenido de la tabla
tabla_dict = {
    "ACCIÓN": ["MÁXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO 1"],
    "TERROR": ["LA MONJA", "LA MALDICIÓN", "EL CONJURO"],
    "DEPORTES": ["ESPN", "MÁS DEPORTE", "ACCIÓN DEPORTE"]
}

# Imprimir la información de la lista
print("Contenido de la lista:")
for item in tabla_contenido:
    print(item)

# Imprimir la información del diccionario
print("\nContenido del diccionario:")
for categoria, peliculas in tabla_dict.items():
    print(f"{categoria}:")
    for pelicula in peliculas:
        print(f"  - {pelicula}")
