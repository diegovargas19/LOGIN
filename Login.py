#Login de usuario
#Vargas Gonzalez Diego Alejandro
#07 de marzo 2023

from tkinter import*
from tkinter import ttk


class Login:
    #init es el tipo constructor de la clase
    def __init__(self, raiz):#raiz = root
        raiz.title("Inicio de sesion")

        mainFrame = ttk.Frame(raiz, padding="10 10 10 10")#izquierda arriba derecha abajo
        mainFrame.grid(column=0, row=0)
        
        usuarioEntry = ttk.Entry(mainFrame, width=30)
        usuarioEntry.grid(column=1, row=0, pady=12, sticky=(W, E))

        contraEntry = ttk.Entry(mainFrame, width=30)
        contraEntry.grid(column=1, row=2, pady=12, sticky=(W, E))
        
        ttk.Label(mainFrame, text="Usuario:  ").grid(column=0, row=0, pady=12, sticky=(E))
        ttk.Label(mainFrame, text="Contraseña:  ").grid(column=0, row=2, pady=12, sticky=(E))

        ttk.Button(mainFrame, text="Ingresar",).grid(column=1, row=5, pady=12, sticky=(E))
        usuarioEntry.focus()
        
if __name__=="__main__":
    print("Este es el archivo principal.")
    print("Nada mas se mostrara este mensaje si es el principal")