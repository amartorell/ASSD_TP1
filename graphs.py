from tkinter import *
import matplotlib, sys
matplotlib.use('TkAgg')
import math
import scipy
from scipy import signal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.pyplot import plot,xscale,show
import matplotlib.patches as patches
from tkinter import ttk

#root = Tk()

class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("ASSD: Entorno de Simulacion")
        self.root.resizable(False,False)
        self.ventana_izquierda = Frame(self.root)
        self.ventana_izquierda.grid()

        self.ventana_derecha = Frame(self.root)
        self.ventana_derecha.grid(row=0,column=1)

        self.ventana_inferior = Frame(self.root)
        self.ventana_inferior.grid(row=1)


        self.label_1 = Label(self.ventana_derecha,text="Caracteristicas de la señal:")
        self.label_1.grid(row=0,column=0,columnspan=2)

        self.label_2 = Label(self.ventana_derecha,text="Aca no se que poner")
        self.label_2.grid(row=5,column=0)

        SignalList = ('3/2 Seno', 'Cuadratica', 'Cuadrada', 'Triangular')
        self.SignalInputString = StringVar()
        self.SignalInputString.set(SignalList[0])
        InputSignalMenu = OptionMenu(self.ventana_derecha, self.SignalInputString, *SignalList)
        InputSignalMenu.grid(row=1, column=0)

        self.Frecuency = Scale(self.ventana_derecha, from_=150, to=15000, resolution=1, label='Frecuency:', orient=HORIZONTAL)
        self.Frecuency.set(1500)
        self.Frecuency.grid(row=2, column=0, padx=5, pady=5)

        self.Voltage = Scale(self.ventana_derecha, from_=-5, to=5, resolution=0.1, label='Vpp:', orient=HORIZONTAL)
        self.Voltage.set(5)
        self.Voltage.grid(row=3, column=0, columnspan=1, padx=5, pady=5)

        self.DutyCycle = Scale(self.ventana_derecha, from_=5, to=95, resolution=5, label='Duty Cycle:', orient=HORIZONTAL)
        self.DutyCycle.set(50)
        self.DutyCycle.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

        self.check_faa = IntVar()
        self.CheckFAA = Checkbutton(self.ventana_derecha, text="FAA", variable=self.check_faa)
        self.CheckFAA.grid(row=6,column=0)

        self.check_sample_and_hold = IntVar()
        self.CheckSAH = Checkbutton(self.ventana_derecha, text="Sample and Hold", variable=self.check_sample_and_hold, command=self.mostrar_config)
        self.CheckSAH.grid(row=6,column=2,columnspan=2,padx=8,pady=8)

        self.Frecuencia_SH=Scale(self.ventana_derecha, from_=150, to=15000, label='Frecuencia S&h', orient=HORIZONTAL)
        self.Frecuencia_SH.set(1000)

        self.Duty_SH=Scale(self.ventana_derecha, from_=5, to=95, label='Duty cycle S&H', orient=HORIZONTAL)
        self.Duty_SH.set(50)

        self.check_llave_analog = IntVar()
        self.CheckANKEY = Checkbutton(self.ventana_derecha, text="Llave analogica", variable=self.check_llave_analog)
        self.CheckANKEY.grid(row=6,column=4,columnspan=2,padx=8,pady=8)

        self.check_fr = IntVar()
        self.CheckFR = Checkbutton(self.ventana_derecha, text="FR", variable=self.check_fr)
        self.CheckFR.grid(row=6,column=6,columnspan=2,padx=8,pady=8)

        self.GraphButtom = Button(self.ventana_derecha, text="Graficar", command=self.Graficar)
        self.GraphButtom.grid(row=10,column=6,columnspan=2)




# ------------------------------------------------------------------------------------------------
# metiendo el grafico
        graph = Canvas(self.ventana_izquierda)
        graph.grid(row=1, columnspan=1000, padx=10, pady=10)
        f = Figure()
        self.axis = f.add_subplot(111)

        self.dataPlot = FigureCanvasTkAgg(f, master=graph)
        self.dataPlot.draw()
        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        self.nav = NavigationToolbar2Tk(self.dataPlot, self.ventana_inferior)
        self.nav.update()
        self.dataPlot._tkcanvas.pack(side=TOP, expand=True)
#--------------------------------------------------------------------------------------------------


        self.root.mainloop()

    def Graficar(self):
        print("hacer algo wachin")


    def mostrar_config(self):
        if (self.check_sample_and_hold.get()):
            self.Frecuencia_SH.grid(row=7, column=3, padx=8, pady=8)
            self.Duty_SH.grid(row=8,column=3,padx=8,pady=8)
        else:
            self.Frecuencia_SH.grid_remove()
            self.Duty_SH.grid_remove()


b = GUI()



#def printName():
#    print("tu vieja en tanga")

#button1 = Button(root, text="button 1", fg="red",command=printName)
#button1.pack()


#root.mainloop()
