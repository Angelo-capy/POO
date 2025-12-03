from tkinter import *

ventana=Tk()
ventana.title("Uso de label")
ventana.geometry("800x600")

#Etiqueta o label
etiqueta1=Label(ventana, text="Nombre de la Persona", font=("papyrus", 20)).pack()
marco1=Frame(ventana, bg="red", width=500, height=100)
marco1.pack_propagate(False)
marco1.pack()

marco2=Frame(marco1, bg="blue", width=100, height=50).pack()
etiqueta2=Label(marco1, text="Soy una etiqeuta dentro de un marco", font=("papyrus", 15)).pack()



ventana.mainloop()