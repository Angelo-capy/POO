import os

os.system("cls")

class Fabrica:
    def __init__(self, ruedas, color, precio):
        self._ruedas = ruedas
        self._color = color
        self._precio = precio

    @property
    def ruedas(self):
        return self._ruedas
    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    @property
    def color(self):
        return self._ruedas
    @color.setter
    def ruedas(self, color):
        self._ruedas = color

    @property
    def precio(self):
        return self._ruedas
    @precio.setter
    def ruedas(self, precio):
        self._ruedas = precio


class Moto(Fabrica):
    def __init__(self, ruedas, color, precio):
        super().__init__(ruedas, color, precio)

    def mostrar_llantas(self):
            return f"La moto tiene {self._ruedas} ruedas"

    def mostrar_color(self):
            return f"El color de la moto es {self._color}"
        
    def mostrar_precio(self):
            return f"El precio de la moto es ${self._precio}"

class Carro(Fabrica):
    def __init__(self, ruedas, color, precio):
        super().__init__(ruedas, color, precio)

    def mostrar_llantas(self):
        return f"El auto tiene {self._ruedas} ruedas"

    def mostrar_color(self):
        return f"El color del auto es {self._color}"
    
    def mostrar_precio(self):
        return f"El precio del auto es ${self._precio}"


auto1 = Carro(4, "Rojo", 20000)
print(auto1.mostrar_llantas())
print(auto1.mostrar_color())
print(auto1.mostrar_precio())

print("-------------------------------------------------")

moto1 = Moto(2, "Azul", 15000)
print(moto1.mostrar_llantas())
print(moto1.mostrar_color())
print(moto1.mostrar_precio())