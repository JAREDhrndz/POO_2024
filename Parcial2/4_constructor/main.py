
from coches import *

#Crear un objetos o instanciar la clase
print("Objeto 1")
coche1=Coches()

#Mostrar los valores inicales del objeto o instancia de la clase
# print(f"Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y un potencia de {coche1.caballaje} hp")
coche1.getInfo()

#Utilizar los metodos set para cambiar o modificar los valores de los atributos aun cuando tengan un valor o no ... aunque los valores solo cambiaran para el objeto o instancia en cuestion en el momento que otro objeto se crea si se tienen valores iniciales se crea con los valores de los atributos de clase 

#actualizar todas las propiedades de objeto
coche1.setColor("Amarillo")
coche1.setModelo("2020")
coche1.setMarca("Porsche")
coche1.setVelocidad(250)
coche1.setCaballaje(450)
coche1.setPlazas(2)


#Aunque con los atributos se puede mostrar un valor se recomienda que sea a traves de los getters
# print(f"Marca: {coche1.getMarca()} {coche1.getColor()}, numeros de plazas: {coche1.getPlazas()} \nModelo: {coche1.getModelo()} con una velocidad de {coche1.getVelocidad()} Km/h y un potencia de {coche1.getCaballaje()} hp")
coche1.getInfo()

#Crear otro objeto e imprimir los valores
print("Objeto 2")
coche2=Coches("Azul","Nissan","2020",100,150,6)

#Imprimir los valores del otro objeto
# print(f"Marca: {coche2.getMarca()} {coche2.getColor()}, numeros de plazas: {coche2.getPlazas()} \nModelo: {coche2.getModelo()} con una velocidad de {coche2.getVelocidad()} Km/h y un potencia de {coche2.getCaballaje()} hp")
coche2.getInfo()
