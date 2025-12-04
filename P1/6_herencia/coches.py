import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #Metiodo constructor para inicializar los valores de los atributos a la hora de crear o instanciar el objeto de la clase

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas

    #Crear los metodos setters y getters, estos metodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los atributos a traves de estos metodos. . . digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto
    #En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    #1er forma
    def getMarca(self):
        return self.__marca
    def setMarca(self, marca):
       self.__marca=marca

    def getColor(self):
        return self.__color
    
    def setColor(self, color):
       self.__color=color

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self, modelo):
       self.__modelo=modelo

    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self, velocidad):
       self.__velocidad=velocidad

    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self, caballaje):
        self.__caballaje=caballaje

    def getPlazas(self):
        return self.__plazas
    
    def setPlazas(self, plazas):
        self.__plazas=plazas
    #Metodos o acciones o funciones que hace el objeto
    def acelerar(self):
        return "El coche esta acelerando"

    def frenar(self):
      return "El coche esta frenando"

#Fin definir clase

#Crear un objetos o instanciar la clase

class otra: 
    pass

def esperarTecla():
    input("\nPresione una tecla para continuar...")
    os.system("cls")

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

        def cargar(self, tipo_carga):
            self.tipo_carga=tipo_carga
            return self.tipo_carga
        
        def acelerar(self):
            return "El camion esta acelerando"
        
        def frenar(self):
            return "El camion esta frenando"
        
        @property
        def eje(self):
            return self.__eje
        
        @eje.setter
        def eje(self, eje):
            self.__eje=eje

        @property
        def capacidadCarga(self):
            return self.__capacidadCarga
        
        @capacidadCarga.setter
        def capacidadCarga(self, capacidadCarga):
            self.__capacidadCarga=capacidadCarga

class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada

        def transportar(self,num_pasajeros):
            self.num_pasajeros=num_pasajeros
            return self.num_pasajeros
        
        def acelerar(self):
            return "La camioneta esta acelerando"
        
        def frenar(self):
            return "La camioneta esta frenando"
        
        @property
        def traccion(self):
            return self.__traccion
        
        @traccion.setter
        def traccion(self, traccion):
            self.__traccion=traccion

        @property
        def cerrada(self):
            return self.__cerrada
        
        @cerrada.setter
        def cerrada(self, cerrada):
            self.__cerrada=cerrada