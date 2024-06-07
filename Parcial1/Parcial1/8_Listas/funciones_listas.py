paises=["Mexico","USA","BRASIL","China"]
numeros=[100,80,3.1416,75]
varios=["UTD", True, 100,0.100]

#ordenar paises
print(paises)
paises.sort()
print(paises)

#ordenar numeros
print(numeros)
numeros.sort()
print(numeros)

#agregar elementos a la lista
print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)


#remover
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(2)

#Dar la vuelta a los elementos de una lista
print(varios)
varios.reverse()

#Buscar un dato de una lista
encontro="BRASIL" in paises
print(encontro)

#vaciar unalisa
print(paises)
paises.clear()
print(paises)

#unir listas
print(varios)
varios.extend(numeros)
print(varios)
    