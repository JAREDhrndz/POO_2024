#Funcion que no recibe parametros y no regresa valor
def sumaNum1():

    n1=int(input("Numero 1: "))
    n2=int(input("Numero 2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

#sumaNum1()


#Funcion que no recibe parametros y regresa valor
def sumaNum2():

    n1=int(input("Numero 1: "))
    n2=int(input("Numero 2: "))
    suma=n1+n2
    return (f"{n1}+{n2}={suma}")

#print(sumaNum2())


#Funcion que recibe parametros y no regresa valor
def sumaNum3(n1,n2):

    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

#num1=int(input(Numero 1: ))
#num2=int(input(Numero 2: ))
sumaNum3(num1,num2)

#Funcion que recibe parametros y regresa valor
def sumaNum4(n1,n2):
    suma=n1+n2
    return (f"{n1}+{n2}={suma}")

#num1=int(input(Numero 1: ))
#num2=int(input(Numero 2: ))
#print(sumaNum4(num1,num2))


#--------TAREA---------
#crear un programa que solicite a traves de una función la siguiente informacion: 
#nombre del paciente, edad, estatura, tipo de sangre.