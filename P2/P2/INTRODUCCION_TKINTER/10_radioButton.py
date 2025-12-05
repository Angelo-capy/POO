from tkinter import *

ventana=Tk()

def mostrarOpcion():
    resultado.config(text=f"opcion seleccionada: {opcion.get()}")

ventana.title("Radio Button")
ventana.geometry("500x500")

opcion= StringVar()

opcion1= Radiobutton(ventana, text="Opcion 1", font=("times new roman", 12), variable=opcion, value="Opcion 1")
opcion1.pack()
opcion2= Radiobutton(ventana, text="Opcion 2", font=("times new roman", 12), variable=opcion, value="Opcion 2")
opcion2.pack()
opcion3= Radiobutton(ventana, text="Opcion 3", font=("times new roman", 12), variable=opcion, value="Opcion 3")
opcion3.pack()

boton= Button(ventana, text="mostrar opción",font=("times new roman", 12), command=mostrarOpcion)
boton.pack()

resultado= Label(ventana, text="")
resultado.pack()

ventana.mainloop()