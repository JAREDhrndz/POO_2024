#Es la forma en la que que tienen los lenguajes de programación 
#para evitar que sucedan errores en momento de ejecución

#Ejemplo 1: Error cuando una variable no se genera
try:
    nombre = input ("Introduce un nombre: ");

    if len(nombre)>1:
        nombre_usuario("El nombre de usuario es: "+nombre);

    print(nombre_usuario);
except:
    print("Es necesario introducinr un nombre de usuario");

#Ejemplo 2: Error cuando se solicita un numero y se introduce una letra
try:   
    numero=int(input("Dame un numero: "));

    if numero>0:
        print("Soy un numero entero positivo");
    else:
        print("Soy un numero entero negativo");
except:
    print("No se puede convertir a numero entero")
else:
    print("Todo se ejecuto sin errores")
#ValueError

#Ejemplo 3: Cuando se generan multiples excepciones
try:
    num=int(input("Dame un numero: "))
    print("El cuadrado es: " + str(num*num))
except ValueError:
    print("Debes de introducir un numero, no se puede convertir un caracter que no sea numero")
except TypeError:
    print("No es posible convertir el numero a entero")
else:
    print("Finalizo corectamente")
finally:
    print("Finalizó el proceso")