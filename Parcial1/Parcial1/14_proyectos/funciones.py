def insertarPelicula(peliculas):
    pelicula = input("Ingrese el nombre de la película: ")
    peliculas.append(pelicula)
    espereTecla()

def eliminarPelicula(peliculas):
    pelicula = input("Ingrese el nombre de la película a eliminar: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print("Película eliminada exitosamente.")
    else:
        print("La película no se encuentra en la lista.")
    espereTecla()

def actualizarPelicula(peliculas):
    pelicula = input("Ingrese el nombre de la película a actualizar: ")
    if pelicula in peliculas:
        index = peliculas.index(pelicula)
        nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
        peliculas[index] = nuevo_nombre
        print("Nombre de película actualizado correctamente.")
    else:
        print("La película no se encuentra en la lista.")
    espereTecla()

def consultarPeliculas(peliculas):
    print("Peliculas disponibles:")
    for pelicula in peliculas:
        print(pelicula)
    espereTecla()

def buscarPelicula(peliculas):
    pelicula_buscada = input("Ingrese el nombre de la película a buscar: ")
    if pelicula_buscada in peliculas:
        print(f"La película '{pelicula_buscada}' se encuentra en la lista.")
    else:
        print("La película no se encuentra en la lista.")
    espereTecla()

def vaciarLista(peliculas):
    peliculas.clear()
    print("Lista de películas vaciada correctamente.")
    espereTecla()

def espereTecla():
    input("Presione Enter para continuar...")
