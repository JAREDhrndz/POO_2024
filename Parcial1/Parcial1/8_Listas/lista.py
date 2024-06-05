#Crear una lista con valores numericos enteros e imprimir la lista

numeros=[23,34]
print(numeros)


#for i in numeros:
    #print(i)

i=0

while i < len(numeros):
    print(numeros[i])
    i+=1

#crear una lista de palabras, posteriormente ingresar una palabra 
#para buscar la coincidencia en la lista e indicar la posicion de 
#la palabra en caso contrario indiciar 1 vez si no la encontró.

# palabras=["hola","2024","10.23","True"]
# buscar_p=input("Ingrese la palabra a buscar: ")

# no=True
# for i in palabras:
#     if buscar_p==i:
#         print(f"Se encontro la palabra {buscar_p} en la posición: {palabras.index(i)}")
#         no=False

# if no:
#     print(f"No se encontró la palabra")

#CON WHILE
palabras=["hola","2024","10.23","True"]
buscar_p=input("Ingrese la palabra a buscar: ")

i=0

while i == len(buscar_p):
    print(numeros[i])
    i+=1