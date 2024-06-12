lista = []

# Añadir valores a la lista mientras su longitud sea menor a 120
while len(lista) < 120:
    # Por simplicidad, añadimos el valor del tamaño actual de la lista
    lista.append(len(lista) + 1)

# Mostrar la lista usando un bucle for
print("Lista de valores:")
for valor in lista:
    print(valor)
