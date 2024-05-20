
#ciclo while es Estructura interativa que se ejecuta x veces siempre y cuando 
#la condicion se cumplas y se seguira ejecutando tentas veces como sea 
#true la condicion

#sintaxis 
#while condition a
    #bLoque de instricciones


#crear un programa que imprima 5 veces el @
i=1
while i<=5:
    print("@")
    i+=1
   
#crear un programa que imprima los numeros del uno al 5 y los sume 
#y que al final imprima la suma 

i=1
n=0
while i<=3:
     print(i)
     n+=i
     i+=1


print(f"La suma es: {n}")


#Crear un programa que imprima la tabla de multiplicar que el usuario desee

tabla=int(input("ingrese un numero para calcular su tabla de multiplicar: "))

i=1
n1=0

while i<=10:
     n1=i*tabla
     print(f"{tabla} x {i} = {n1}")
     i+=1