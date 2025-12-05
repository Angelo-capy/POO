from tkinter import messagebox
from tkinter import *
from view import interfaz

def sumar(entrada1, entrada2, resultado):
    resultado = entrada1 + entrada2
    return resultado



def restar(entrada1, entrada2, resultado):
    resultado = entrada1 - entrada2
    return resultado



def mulriplicar(entrada1, entrada2, resultado):
    resultado = entrada1 * entrada2
    return resultado



def dividir(entrada1, entrada2, resultado):
    resultado = entrada1 / entrada2
    return resultado

def mostrar_resultado(resultado):
    messagebox.showinfo("Resultado", resultado)






