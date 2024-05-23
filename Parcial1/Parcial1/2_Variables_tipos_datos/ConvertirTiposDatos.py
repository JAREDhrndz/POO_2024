"""
nota: a la hora de concatenar cadenas no es posible inculir en algunas ocasiones contenido de 
variables que no sean del tipo de dato str 
"""

#contatenar un str con str 


texto="soy una cadena de texto"
numero=23

print(texto +" y soy otra cadena :)")



texto="soy una cadena de texto"
numero=23

numero_str=str(numero)

print("El numero: "+numero_str) 

print("El numero: "+str(numero)) 

#contatenar un str con int 

n1='23'
n2=33

suma=int(n1)+n2

print("El numero: "+str(suma))

#contatenar un float y int con str

n1='23'
n2=33.0

suma= int(n1)+n2

print("El numero: "+str(int(suma)))

print(f"El numero:",{suma})

#concatenar float y float con float 

n1='23.34'
n2='33.99'

suma=float(n1)+float(n2)

print(f"El numero es:",{suma})







