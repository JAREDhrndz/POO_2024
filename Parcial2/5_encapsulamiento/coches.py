""""
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

8 METODO CONSTRUCTOR.- Este metodo especial dentro de una clase y se utiliza para dar-un valora los atributos del objeto al crearlo, es el primer metodo que se. ejecuta-al-crear el objeto y se manda llamar automaticamente al crearlo, es. decir este metodo puede recibir parametros al momento de crear el objeto

9

10 Cuando-se crear-un metodo constructor se utiliza la funcion init(), para que se llame automáticamente cada vez que se utiliza la clase para crear un nuevo objeto.

El-self es un parámetro es una referencia a la instancia actual de la clase.y. utiliza-para-acceder a variables que pertenecen a la clase.



el encapsulamiento o visibilidad es importante a travez de el es posible que python sepa como se va a utilizar y manipular los atributos y metodos de la clase





#atributo publico 

atributo_publico=


"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
  def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas

        #atributo publico 
  #atributo publico 

  atributo_publico="soy un atributo publico"
  

   #atributo privddo
  __atributo_privado="soy un atributo privado"

  #atributo privado en metodo publico 

  def metodopublico(self):
      return self.__atributo_privado  

  #metodo privado 

  def __metodoprivado(self):
      print("soy un metodo privado")
    
  #para utilizar un metodo privado es necesario usarlo dentro de un metodo publico
  def getMetodoPublico(self):
      self.__metodoprivado()  
    
    
    #Metodos o acciones o funciones que hace el objeto 

  def acelerar(self):
        self.velocidad+=1

  def frenar(self):
        self.velocidad-=1


    #Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion



  def getColor(self):
      return self.color

  def setColor(self,color):
      self.color=color 

  def getMarca(self):
      return self.marca

  def setMarca(self,marca):
      self.marca=marca 

  def getModelo(self):
      return self.modelo

  def setModelo(self,modelo):
      self.modelo=modelo        

  def getVelocidad(self):
       return self.velocidad

  def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

  def getCaballaje(self):
       return self.caballaje

  def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

  def getPlazas(self):
       return self.plazas

  def setPlazas(self,plazas):
      self.plazas=plazas 

  def getInfo(self):
       print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {coche1.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")  

#Fin definir clase

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
coche2=Coches()

#Imprimir los valores del otro objeto
# print(f"Marca: {coche2.getMarca()} {coche2.getColor()}, numeros de plazas: {coche2.getPlazas()} \nModelo: {coche2.getModelo()} con una velocidad de {coche2.getVelocidad()} Km/h y un potencia de {coche2.getCaballaje()} hp")
coche2.getInfo()

print("Objeto 3")
coche3=Coches()

# print(f"Marca: {coche3.getMarca()} {coche3.getColor()}, numeros de plazas: {coche3.getPlazas()} \nModelo: {coche3.getModelo()} con una velocidad de {coche3.getVelocidad()} Km/h y un potencia de {coche3.getCaballaje()} hp")
coche3.getInfo()