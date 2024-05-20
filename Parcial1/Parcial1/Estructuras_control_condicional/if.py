"""
Existe una estructura de control llamada "if"
la cual evalua una condicion para encontrar el valor "True" y si se cumple la condicion 
se ejecuta la linea o lineas de codigo 

4 variaantes 

1.- if simple
2.-if compuesto 
3.-if anidado 
4.-if y elif 
"""


color= input("Ingrese un color: ")
if color=="rojo":
 print("soy el color rojo")

#if compuesto 
color= input("Ingrese un color: ")
if color=="rojo":
 print("soy el color rojo")
else:
 print("soy otra cosa")

#if anidado 
color= input("Ingrese un color: ")
if color=="rojo":
 print("soy el color rojo")
if color!="rojo":
  print("NO soy el color rojo")
else:
 print("soy otra cosa")

#IfElif 
if color=="rojo":
 print("soy el color rojo")
elif color=="Amarillo":
  print("soy el color Amarillo")
elif color=="azul":
  print("soy el color Azul")
elif color=="morado":
  print("soy el color Morado")
else:
  print("No soy ningun color de los anteriores")


#crear un programa que solicite el numero de la semana e imprima en pantalla el dia que le corresponde

Dia=int(input("Ingrese el dia de la semana"));

if Dia==1:
  print("Domingo")
elif Dia==2:
  print("Lunes")
elif Dia==3:
  print("Martes")
elif Dia==4:
  print("Miercoles")
elif Dia==5:
  print("Jueves")
elif Dia==6:
  print("Viernes")
elif Dia==7:
  print("sabado")
else:
  print("No corresponde a un dia de la semana")