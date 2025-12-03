from tkinter import *
from tkinter import messagebox
from controller import funciones
# Interfaz o VIEW 


"""
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

class Vista:
     def __init__(self, ventana):
          ventana.title("Calculadora POO")
          ventana.geometry("600x400")
          ventana.resizable(False, False)

     def calcular(operacion, n1, n2):
        if operacion == "suma":
            resultado = n1 + n2
            mensaje = f"{n1} + {n2} = {resultado}"
        elif operacion == "resta":
            resultado = n1 - n2
            mensaje = f"{n1} - {n2} = {resultado}"
        elif operacion == "multiplicacion":
            resultado = n1 * n2
            mensaje = f"{n1} x {n2} = {resultado}"
        elif operacion == "division":
            resultado = n1 / n2
            mensaje = f"{n1} / {n2} = {resultado}"


        return messagebox.showinfo("Resultado", mensaje)


     def interfaz_principal(self, ventana):
        n1=IntVar()
        n2=IntVar()
        txt_numero1=Entry(ventana, textvariable=n1, width=5, justify=CENTER)
        txt_numero1.pack(side="TOP", anchor="CENTER")
        txt_numero2=Entry(ventana, textvariable=n2, width=5, justify=CENTER)
        txt_numero2.pack(side="TOP", anchor="CENTER")
        



