print("MENU DE OPCIONES \n 1-SUMA \n 2-RESTA \n 3-MULTIPLICACIÓN \n 4-DIVISIÓN \n 5-SALIR")
opcion=("Elige una opción: ").upper

n1=int (intpuinput("Numero 1: "))
n2=int (intpuinput("Numero 2: "))


if opcion=="1" or opcion=="SUMA" or opcion=="+":
    print(f"{n1}+{n2}={n1+n2}")

elif opcion=="2" or opcion=="RESTA" or opcion=="-":
    print(f"{n1}-{n2}={n1-n2}")

elif opcion=="3" or opcion=="MULTIPLICACION" or opcion=="*":
    print(f"{n1}*{n2}={n1*n2}")

elif opcion=="4" or opcion=="DIVISION" or opcion=="/":
    print(f"{n1}/{n2}={n1/n2}")

#else:
    #print("SALISTE DEL PROGRAMA")