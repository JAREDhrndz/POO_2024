numeros = [8, 3, 1, 7, 4, 2, 6, 5]

# a.- Recorrer la lista y mostrarla
print("Lista de números:")
for numero in numeros:
    print(numero)

# b.- Hacer una función que recorra la lista de números y devuelva un string
def lista_a_string(lista):
    return ", ".join(str(num) for num in lista)

# Mostrar el string resultante de la función
print("\nLista de números como string:")
print(lista_a_string(numeros))

# c.- Ordenarla y mostrarla
numeros_ordenados = sorted(numeros)
print("\nLista de números ordenada:")
print(numeros_ordenados)

# d.- Mostrar su longitud
print("\nLongitud de la lista:")
print(len(numeros))

# e.- Buscar algún elemento que el usuario pida por teclado
elemento_a_buscar = int(input("\nIntroduce el número que deseas buscar en la lista: "))
if elemento_a_buscar in numeros:
    print(f"El número {elemento_a_buscar} está en la lista.")
else:
    print(f"El número {elemento_a_buscar} no está en la lista.")
