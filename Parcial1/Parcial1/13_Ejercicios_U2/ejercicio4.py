una_lista = [1, 2, 3, 4]
una_cadena = "Hola, mundo"
un_entero = 42
un_logico = True

# Definición de funciones para imprimir mensajes según el tipo de dato
def mensaje_tipo_dato(variable):
    if isinstance(variable, list):
        print("La variable es una lista.")
    elif isinstance(variable, str):
        print("La variable es una cadena de texto.")
    elif isinstance(variable, int):
        print("La variable es un entero.")
    elif isinstance(variable, bool):
        print("La variable es un valor lógico.")
    else:
        print("La variable es de un tipo desconocido.")

# Llamar a la función para cada variable
mensaje_tipo_dato(una_lista)
mensaje_tipo_dato(una_cadena)
mensaje_tipo_dato(un_entero)
mensaje_tipo_dato(un_logico)
