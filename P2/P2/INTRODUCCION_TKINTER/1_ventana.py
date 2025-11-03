'''
Tkinter trabaja a traves de interfaces, es una biblioteca de python que permite crear
aplicaciones en python para escritorio
'''

import tkinter as tk 

ventana=tk.Tk() #Crear una ventana

ventana.title("Mi primera ventana")#Titulo de la ventana
ventana.geometry("800x600")#tamaño de la ventana
ventana.resizable(True, True)#Permitir cambiar el tamaño de la ventana (ancho, alto)
ventana.mainloop()#Permite mantener la ventana abierta
