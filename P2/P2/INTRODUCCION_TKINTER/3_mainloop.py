from tkinter import *

ventana=Tk()
ventana.geometry("800x600")
ventana.title("Main-loop")


marco=Frame(ventana)
marco.config(width=600, height=400, bg="#0AE5F0", border=100, relief= RAISED)
marco.pack(padx=50, pady=100)


ventana.mainloop()