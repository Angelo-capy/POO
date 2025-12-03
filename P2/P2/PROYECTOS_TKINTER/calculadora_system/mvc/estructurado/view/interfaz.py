from tkinter import *
from tkinter import messagebox
from controller import funciones
# Interfaz o VIEW 


def interfaz_principal():

    ventana = Tk()

    ventana.title("Calculadora Normal")
    ventana.geometry("600x400")


    n1 = StringVar() 
    n2 = StringVar()
    operacion = StringVar()
    

    entrada1 = Entry(ventana, textvariable=n1, width=10, justify="right")
    entrada1.pack(pady=5)

    entrada2 = Entry(ventana, textvariable=n2, width=10, justify="right")
    entrada2.pack(pady=5)

    frame_operaciones = Frame(ventana) 
    frame_operaciones.pack(pady=10)

    btn_sumar = Button(frame_operaciones, text="+", command=lambda: funciones.sumar(n1.get(), n2.get()))
    btn_sumar.pack(side=LEFT)

    btn_restar = Button(frame_operaciones, text="-", command=lambda: funciones.restar(n1.get(), n2.get()))
    btn_restar.pack(side=LEFT)

    btn_multiplicar = Button(frame_operaciones, text="x", command=lambda: funciones.multiplicar(n1.get(), n2.get()))
    btn_multiplicar.pack(side=LEFT)

    btn_dividir = Button(frame_operaciones, text="/", command=lambda: funciones.dividir(n1.get(), n2.get()))
    btn_dividir.pack(side=LEFT)

    btn_salir = Button(ventana, text="Salir", command=ventana.quit)
    btn_salir.pack(pady=10)

    #messagebox para la salida de resultados


    ventana.mainloop()
