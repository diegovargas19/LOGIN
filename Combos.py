from tkinter import*
from tkinter import ttk

raiz = Tk()

comida = StringVar()
 
comboComida = ttk.Combobox(raiz, textvariable=comida)
comboComida.grid()
comboComida['values']=("Pizza", "Pozole", "Hamburguesa", "Galletas")

raiz.mainloop()