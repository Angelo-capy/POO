from tkinter import *

ventana=Tk()

ventana.title("Frame en Tkinter")
ventana.geometry("800x600")

#marcos
marco=Frame(ventana,width=300,height=200,bg="silver",borderwidth=2,relief=SOLID)  
marco.pack_propagate(False)#Evitar que el marco se ajuste a los elementos internos
marco.pack(pady=165)

marco2=Frame(marco,width=200,height=100,bg="red",border="2", relief=GROOVE).pack(padx=50, pady=50)

ventana.mainloop()