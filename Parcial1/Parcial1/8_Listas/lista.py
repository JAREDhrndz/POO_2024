# #Crear una lista con valores numericos enteros e imprimir la lista

# numeros=[23,34]
# print(numeros)


# #for i in numeros:
#     #print(i)

# i=0

# while i < len(numeros):
#     print(numeros[i])
#     i+=1

# #crear una lista de palabras, posteriormente ingresar una palabra 
# #para buscar la coincidencia en la lista e indicar la posicion de 
# #la palabra en caso contrario indiciar 1 vez si no la encontró.

# # palabras=["hola","2024","10.23","True"]
# # buscar_p=input("Ingrese la palabra a buscar: ")

# # no=True
# # for i in palabras:
# #     if buscar_p==i:
# #         print(f"Se encontro la palabra {buscar_p} en la posición: {palabras.index(i)}")
# #         no=False

# # if no:
# #     print(f"No se encontró la palabra")

# #CON WHILE
# palabras=["hola","2024","10.23","True"]
# buscar_p=input("Ingrese la palabra a buscar: ")

# i=0

# while i < len(buscar_p):
#     print(numeros[i])
#     i+=1

#crear una lista multidimensional (matriz) para crear una agenda

agenda=[
 ["Carlos", 6181354710],
 ["Dago", 6189895415],
 ["Jared", 6181932110],
]

for i in agenda:
     print(f"{agenda.index(i)+1}.-{i}")
    
#crear un prgrama que permita gestionar  peliculas, colocar un menu de opciones para agregar, remover, consultar peliculas.
#notas utilizar funciones y mandar llamar desde otro archivo 
#utilizar linea para alamcenar los nombres de las peliculas 

def insertarPeliculas():
    peliculas=input("Ingrese la pelicula: ")
    peliculas.append(pelicula)
    espereTecla()

def removerPeliculas():
    peliculas=input("Ingrese la pelicula: ")
    peliculas.remove(pelicula)
    espereTecla()

peliculas=[]

print("1-Agregar \n2-Remover \n3-Consulta \n4-SALIR")
opcion=input("\t Elige una opcion: ").upper()

if opcion=="1" or opcion=="AGREGAR":
    insertarPeliculas()

if opcion=="2" or opcion=="REMOVER":
    removerPeliculas()

    #carpetas
    #google
    #practica