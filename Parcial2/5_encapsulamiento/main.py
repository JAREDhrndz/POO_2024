from coches import *




print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
# coche1.getInfo()



# print("Objeto 2")
# coche2=Coches("Azul","Nissan","2020",180,150,6)
# coche2.setcolor("Blue Demon")
# coche2.getInfo()


print(coche1.atributo_publico)



print(coche1.metodopublico)



coche1.__metodoprivado()


coche1.getMetodoPublico()