import math

print("MENU DE OPCIONES \n 1-SUMA \n 2-RESTA \n 3-MULTIPLICACIÓN \n 4-DIVISIÓN \n 5-RAIZ \n 6-POTENCIA  \n 7-SALIR")
opcion = input("Elige una opción: ").upper()

if opcion == "1" or opcion == "SUMA" or opcion == "+":
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(f"{n1}+{n2}={n1+n2}")

elif opcion == "2" or opcion == "RESTA" or opcion == "-":
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(f"{n1}-{n2}={n1-n2}")

elif opcion == "3" or opcion == "MULTIPLICACION" or opcion == "*":
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(f"{n1}*{n2}={n1*n2}")

elif opcion == "4" or opcion == "DIVISION" or opcion == "/":
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(f"{n1}/{n2}={n1/n2}")

elif opcion == "5" or opcion == "RAIZ" or opcion == "√":
    n1 = int(input("Numero: "))
    print(f"√{n1}={math.sqrt(n1)}")

elif opcion == "6" or opcion == "POTENCIA" or opcion == "^":
    n1 = int(input("Numero: "))
    n2 = int(input("Potencia: "))
    print(f"{n1}^{n2}={n1**n2}")

else:
    print("SALISTE DEL PROGRAMA")
