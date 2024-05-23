#ciclo for Estructura interativa qie se ejecuta x veces 

#sintaxis 
#for (Variables) in (elemento_interable) (lista,rango, etc)
    #bLoque de instricciones


#crear un programa que imprima 5 veces el @

i=1  

for i in range(1,6):
    print("@")
   
#crear un programa que imprima los numeros del uno al 5 y los sume 
#y que al final imprima la suma 


n=0
for i in range (1,5):
    print(i)
    n+=i

print(f"La suma es: {n}")


#Crear un programa que imprima la tabla de multiplicar que el usuari desee

tabla=int(input("ingrese un numero para calcular su tabla de multiplicar: "))


n1=0
for i in range (1,10):
    n1=i*tabla
    print(f"{tabla} x {i} = {n1}")

