from tkinter import *

def mostrarEstado():
    if opcion.get() == 1:
        resultado.config(text=f"Notificaciones activadas ")
    else:
        resultado.config(text=f"Notificaciones desactivadas ")

ventana=Tk()

ventana.title("Check Button")
ventana.geometry("500x500")

opcion= IntVar()
checkbox= Checkbutton(ventana, text="Deseas recibir notificaciones?", variable=opcion, onvalue=1, offvalue=0)
checkbox.pack()


boton= Button(ventana, text="Confirmar", command=mostrarEstado) 
boton.pack()

resultado= Label(ventana, text="")
resultado.pack()

ventana.mainloop()
