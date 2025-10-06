"""
Ejercicio 2: "Modelar y Diagramar en POO"

"""
import os

os.system("cls")

#crear una clase 
class Coches:
    #Metodo constructor que inicializa los valores de los atributos 
    #cuando se instancie un objeto de la clase
    def __init__(self, color, marca, velocidad=0):
        self.color = color
        self.marca = marca
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad=self.velocidad + incremento
        return self.velocidad
    
    def frenar(self, decremento):
        self.velocidad=self.velocidad - decremento
        return self.velocidad
    
    def tocar_claxon():
        return "PIIIIIIII"

#INSTANCIAR OBJETOS DE LA CLASE COCHES

coche1 = Coches("Blanco", "Toyota", 220)
coche2 = Coches("Amarillo", "Nissan", 180)

print(f"Los valores del objeto 1 son: color {coche1.color}, marca {coche1.marca} y {coche1.velocidad} km/h")

print(f"La velocidad original del coche 1 es: {coche1.velocidad} km/h y cambio a {coche1.acelerar(50)} km/h")

print(f"Los valores del objeto 2 son: color {coche2.color}, marca {coche2.marca} y {coche2.velocidad} km/h")

print(f"La velocidad original del coche 2 era de: {coche2.velocidad} km/h y se redujo a {coche2.frenar(80)} km/h")