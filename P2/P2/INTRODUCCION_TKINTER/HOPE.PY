import os

class figuras:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    def estaVisible(self):
        return self.visible
    
    def mostrar(self):
        return f"Figura en ({self.x}, {self.y}), Visible: {self.visible}"
    
    def ocultar(self):
        self.visible = False
        return "Figura oculta"
    
    def mover(self):
        self.x = input("Ingrese nueva coordenada X: ")
        self.y = input("Ingrese nueva coordenada Y: ")
        return f"Figura movida a ({self.x}, {self.y})"
    
    def calcular_area(self):
        area = int(input("Ingrese el area de la figura: "))
        return f"El area de la figura es: {area}"

class Rectangulo(figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.__alto = alto
        self.__ancho = ancho

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def radio(self, alto):
        self.__alto = alto

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def radio(self, ancho):
        self.__ancho = ancho

    def mostrar(self):
        return f"Figura en ({self.x}, {self.y}), Visible: {self.visible}"
    
    def ocultar(self):
        self.visible = False
        return "Figura oculta"
    
    def calcularArea(self):
        area = self.alto * self.ancho
        return f"El area del rectangulo es: {area}"

class Circulo(figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.__radio = radio

    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, radio):
        self.__radio = radio

    def mostrar(self):
        return f"Figura en ({self.x}, {self.y}), Visible: {self.visible}"
    
    def ocultar(self):
        self.visible = False
        return "Figura oculta"
    
    def calcularArea(self):
        area = 3.14 * (self.radio ** 2)
        return f"El area del circulo es: {area}"
    

os.system("cls")

rectangulo1 = Rectangulo(3, 4, True, 10, 20)
print(rectangulo1.calcularArea())
print(rectangulo1.mostrar())
print("-----")


circulo1 = Circulo(3, 3, True, 6)
print(circulo1.calcularArea())
print(circulo1.mostrar())