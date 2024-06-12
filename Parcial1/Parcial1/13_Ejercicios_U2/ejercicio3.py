lista_palabras = []

# Comprobar si la lista está vacía
if not lista_palabras:
    print("La lista está vacía. Puedes añadir palabras o frases.")

    # Bucle para añadir palabras o frases hasta que el usuario decida parar
    while True:
        palabra = input("Introduce una palabra o frase (o escribe 'salir' para terminar): ")
        if palabra.lower() == 'salir':
            break
        lista_palabras.append(palabra)

# Imprimir el contenido de la lista en mayúsculas
print("\nContenido de la lista en mayúsculas:")
for palabra in lista_palabras:
    print(palabra.upper())
