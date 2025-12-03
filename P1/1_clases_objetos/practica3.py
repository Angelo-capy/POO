import os 

os.system("cls")

class Alumnos:

    def __init__(self, nombre, edad, matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula 

    def inscribirse (self):
        print(f"{self.__nombre} se ha inscrito correctamente")
        return
    def estudiar (self): 
        print(f"{self.__nombre} esta estudiando")
        return

class Cursos:

    def __init__(self, nombre, codigo, creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    def asignar (self):
        pass

class Profesores:

    def __init__(self, nombre, experiencia, num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor

    def impartir (self): 
        pass
        
    def evaluar (self):
        pass


alumno1=Alumnos("Juan", 20, "A12345")
alumno2=Alumnos("Maria", 22, "B67890")

curso1=Cursos("Calculo integral", "XSd3481", 6)
curso2=Cursos("Programacion orientada a objetos", "POO2024", 8)


profesor1=Profesores("Raul", 5, "P001")
profesor2=Profesores("Isaac", 3, "A928")

print(f"Datos del Alumno: \n Nombre:{alumno1._Alumnos__nombre} \n Edad: {alumno1._Alumnos__edad} \n Matricula: {alumno1._Alumnos__matricula} ")
print(alumno1.inscribirse())
print("---------------------------------------------------")
print(f"Datos del Alumno: \n Nombre:{alumno2._Alumnos__nombre} \n Edad: {alumno2._Alumnos__edad} \n Matricula: {alumno2._Alumnos__matricula} ")
print(alumno2.estudiar())
print("---------------------------------------------------")
