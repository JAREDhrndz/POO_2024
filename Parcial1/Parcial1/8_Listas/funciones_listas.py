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

#agregar eementos a la lista
print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)


#remover
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(5)
