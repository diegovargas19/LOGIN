#Muestra widgets
#Vargas Gonzalez Diego Alejandro
#09 de marzo 2023

from tkinter import*
from tkinter import ttk


class MuestraWidgets:
    #init es el tipo constructor de la clase
    def __init__(self, raiz):#raiz = root
        raiz.title("Muestra Widgets")

        estado = StringVar()

        mainFrame = ttk.Frame(raiz, padding="10 10 10 10")#izquierda arriba derecha abajo
        mainFrame.grid(column=0, row=0)

        frame1 = ttk.Frame(mainFrame, padding="10 10 10 10", borderwidth=3, relief="raised")
        frame1.grid(column=0, row=0)

        frame2 = ttk.Frame(mainFrame, padding="10 10 10 10", borderwidth=3, relief="raised")
        frame2.grid(column=0, row=1)

        frame3 = ttk.Frame(mainFrame, padding="10 10 10 10")
        frame3.grid(column=1, row=0)
        
        nombreEntry = ttk.Entry(frame1, width=30)
        nombreEntry.grid(column=1, row=0, pady=12, sticky=(W, E))

        aPaternoEntry = ttk.Entry(frame1, width=30)
        aPaternoEntry.grid(column=1, row=2, pady=12, sticky=(W, E))

        aMaternoEntry = ttk.Entry(frame1, width=30)
        aMaternoEntry.grid(column=1, row=3, pady=12, sticky=(W, E))

        correoEntry = ttk.Entry(frame1, width=30)
        correoEntry.grid(column=1, row=4, pady=12, sticky=(W, E))

        movilEntry = ttk.Entry(frame1, width=30)
        movilEntry.grid(column=1, row=5, pady=12, sticky=(W, E))
        
        ttk.Label(frame1, text="Nombre:  ").grid(column=0, row=0, pady=12, sticky=(E))
        ttk.Label(frame1, text="A. Paterno:  ").grid(column=0, row=2, pady=12, sticky=(E))
        ttk.Label(frame1, text="A. Materno:  ").grid(column=0, row=3, pady=12, sticky=(E))
        ttk.Label(frame1, text="Correo:  ").grid(column=0, row=4, pady=12, sticky=(E))
        ttk.Label(frame1, text="Movil:  ").grid(column=0, row=5, pady=12, sticky=(E))

        ttk.Label(frame2, text="Aficiones:  ").grid(column=0, row=0, pady=12, sticky=(E))
        leer = ttk.Checkbutton(frame2, text='leer')
        leer.grid(column=0, row=1, sticky=(W))
        musica = ttk.Checkbutton(frame2, text='musica')
        musica.grid(column=1, row=1, sticky=(W))
        videojuegos = ttk.Checkbutton(frame2, text='videojuegos')
        videojuegos.grid(column=2, row=1, sticky=(W))

        

        comboEstados = ttk.Combobox(mainFrame, textvariable=estado)
        comboEstados.grid(column=1, row=1, pady=50)
        comboEstados['values']=("Estados 32","Jalisco", "Nayarit", "Colima", "Michoacan")
        
        ttk.Button(mainFrame, text="Guardar",).grid(column=0, row=5, pady=12, sticky=(W))
        ttk.Button(mainFrame, text="Cancelar",).grid(column=0, row=5, pady=12, sticky=(N))

        estudiante = ttk.Radiobutton(frame3, text='estudiante')
        estudiante.grid(column=0, row=0, sticky=(W))
        empleado = ttk.Radiobutton(frame3, text='empleado')
        empleado.grid(column=0, row=1, sticky=(W))
        desempleado = ttk.Radiobutton(frame3, text='desempleado')
        desempleado.grid(column=0, row=2, sticky=(W))


        nombreEntry.focus()

        
if __name__=="__main__":
    print("Este es el archivo principal.")
    print("Nada mas se mostrara este mensaje si es el principal")