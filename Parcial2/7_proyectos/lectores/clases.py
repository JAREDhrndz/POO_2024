class lectores:
    def __init__(self, nombre, direccion, tel):
        self.nombre=nombre

    def reservar(self):
        print("Esta reservando el libro por"(self.nombre()))

    def entregar(self):
        print("Esta entregando el libro por"(self.nombre()))


    #GET Y SET
    def setNombre(self,nombre):
        self.nombre=nombre

    def getNombre(self):
        return nombre.nombre

    def setDireccion(self,direccion):
        self.direccion=direccion

    def getDirecciom(self):
        return direccion.direccion

    def setTel(self,tel):
        self.tel=tel

    def getTel(self):
        return nombre.nombre





#------ESTUDIANTE---------

class estudiante(lectores):
    def __init__(self, nombre, direccion, tel, carrera, matricula):
        super().__init__(nombre, direccion,tel)
        self._carrera=carrera
        self._matricula=matricula

#METODOS
    def reservar(self):
        print("Esta reservando el libro el etudiante: "(self.nombre()))

    def entregar(self):
        print("Esta entregando el libro el estudiante"(self.nombre()))
        
            #GET Y SET
    def setCarrera(self,carrera):
        self.nombre=nombre

    def getCarera(self):
        return carrera.carrera

    def setMatricula(self,matricula):
        self.matricula=matricula

    def getMatricula(self):
        return matricula.matricula




#------DOCENTE---------

class docente(lectores):
    def __init__(self, nombre, direccion, tel, modalidad, num_empleado):
        super().__init__(nombre, modalidad,num_empleado)
        self.__modalidad=modalidad
        self.__num_empleado=matricula

#METODOS
    def reservar(self):
        print("Esta reservando el libro el docente: "(self.nombre()))

    def entregar(self):
        print("Esta entregando el libro el docente"(self.nombre()))
        
            #GET Y SET
    def setModalidad(self,modalidad):
        self.modalidad=modalidad

    def getModalidad(self):
        return modalidad.modalidad

    def setNum_empleado(self,num_empleado):
        self.num_empleado=num_empleado

    def getNum_empleado(self):
        return num_empleado.num_empleado