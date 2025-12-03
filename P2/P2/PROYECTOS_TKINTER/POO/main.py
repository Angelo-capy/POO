from view import interfaz
from tkinter import *

def main():
    interfaz.interfaz_principal()

class App:
    # def __init__(self, ventana):
    #     view = interfaz.Vista(ventana)
    @staticmethod
    def main(ventana):
        view = interfaz.Vista(ventana)
        
if __name__ == "__main__":
    ventana=Tk()
    #app=App(ventana)
    App.main(ventana)
    ventana.mainloop()