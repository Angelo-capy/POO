'''
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en una alerta
'''

from tkinter import *
from tkinter import messagebox

# Control App o Controlador
def sumar(entrada1, entrada2):
    resultado = int(txt_entrada1.get()) + int(txt_entrada2.get())
    messagebox.showinfo("Resultado", icon="info" f"La resta es: {resultado}")

def restar(entrada1, entrada2):
    resultado = int(txt_entrada1.get()) - int(txt_entrada2.get())
    messagebox.showinfo("Resultado", f"La resta es: {resultado}")

def multiplicar(entrada1, entrada2):
    resultado = int(txt_entrada1.get()) * int(txt_entrada2.get())
    messagebox.showinfo("Resultado", f"La multiplicación es: {resultado}")

def dividir(entrada1, entrada2):
    resultado = int(txt_entrada1.get()) / int(txt_entrada2.get())
    messagebox.showinfo("Resultado", f"La división es: {resultado}")

# Interfaz o VIEW 
ventana = Tk()

ventana.title("Calculadora Normal")
ventana.geometry("600x400")

n1=IntVar
n2=IntVar

txt_entrada1 = Entry(ventana, textvariable=n1, width=5, justify="right")
txt_entrada1.pack()

txt_entrada2 = Entry(ventana, textvariable=n2, width=5, justify="right")
txt_entrada2.pack()


frame_operaciones = Frame(ventana) 
frame_operaciones.pack()

btn_sumar = Button(frame_operaciones, text="+", command=lambda: sumar(n1.get, n2.get))
btn_sumar.pack(side=LEFT)

btn_restar = Button(frame_operaciones, text="-", command=lambda: restar(n1.get, n2.get))
btn_restar.pack(side=LEFT)

btn_multiplicar = Button(frame_operaciones, text="x", command=lambda: multiplicar(n1.get, n2.get))
btn_multiplicar.pack(side=LEFT)

btn_dividir = Button(frame_operaciones, text="/", command=lambda: dividir(n1.get, n2.get))
btn_dividir.pack(side=LEFT)

btn_salir = Button(ventana, text="Salir", command=ventana.quit)
btn_salir.pack()


ventana.mainloop()

