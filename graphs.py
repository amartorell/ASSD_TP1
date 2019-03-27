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
        self.label_1.grid(row=0,column=2,columnspan=2, sticky=W)

        self.label_2 = Label(self.ventana_derecha,text="Aca no se que poner")
        self.label_2.grid(row=5,column=0)

        self.label_3 = Label(self.ventana_derecha, text='Que ver:')
        self.label_3.grid(row=1, column=5, sticky=W)

        SignalList = ('3/2 Seno', 'Cuadratica', 'Cuadrada', 'Triangular')
        self.SignalInputString = StringVar()
        self.SignalInputString.set(SignalList[0])
        InputSignalMenu = OptionMenu(self.ventana_derecha, self.SignalInputString, *SignalList)
        InputSignalMenu.grid(row=1, column=2)

        self.Frecuency = Scale(self.ventana_derecha, from_=150, to=15000, resolution=1, label='Frecuency:', orient=HORIZONTAL)
        self.Frecuency.set(1500)
        self.Frecuency.grid(row=2, column=2, padx=5, pady=5)

        self.Voltage = Scale(self.ventana_derecha, from_=0, to=5, resolution=0.1, label='Vpp:', orient=HORIZONTAL)
        self.Voltage.set(5)
        self.Voltage.grid(row=3, column=2, columnspan=1, padx=5, pady=5)

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
        self.CheckANKEY = Checkbutton(self.ventana_derecha, text="Llave analogica", variable=self.check_llave_analog, command=self.mostrar_config_LLA)
        self.CheckANKEY.grid(row=6,column=4,columnspan=2,padx=8,pady=8)

        self.frecuencia_LLA = Scale(self.ventana_derecha, from_=150, to=15000, label='Frecuencia', orient=HORIZONTAL)
        self.frecuencia_LLA.set(1000)

        self.duty_cycle_LLA = Scale(self.ventana_derecha, from_=5, to=95, label='Duty cycle', orient=HORIZONTAL)
        self.duty_cycle_LLA.set(50)

        self.check_fr = IntVar()
        self.CheckFR = Checkbutton(self.ventana_derecha, text="FR", variable=self.check_fr)
        self.CheckFR.grid(row=6,column=6,columnspan=2,padx=8,pady=8)

        self.GraphButtom = Button(self.ventana_derecha, text="Graficar", command=self.Graficar)
        self.GraphButtom.grid(row=10,column=6,columnspan=2)

        self.check_frec_graficar = IntVar()
        self.Check_Graph_Frec = Checkbutton(self.ventana_derecha, text='Frecuencia',variable=self.check_frec_graficar)
        self.Check_Graph_Frec.grid(row=2,column=5)

        self.check_tiempo_graficar = IntVar()
        self.Check_Graph_Time = Checkbutton(self.ventana_derecha, text='Tiempo',variable=self.check_tiempo_graficar)
        self.Check_Graph_Time.grid(row=2,column=6)



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
            self.Frecuencia_SH.grid(row=7, column=2, padx=8, pady=8)
            self.Duty_SH.grid(row=8,column=2,padx=8,pady=8)
        else:
            self.Frecuencia_SH.grid_remove()
            self.Duty_SH.grid_remove()

    def mostrar_config_LLA(self):
        if (self.check_llave_analog.get()):
            self.frecuencia_LLA.grid(row=7, column=4, padx=8, pady=8)
            self.duty_cycle_LLA.grid(row=8, column=4, padx=8, pady=8)
        else:
            self.frecuencia_LLA.grid_remove()
            self.duty_cycle_LLA.grid_remove()


b = GUI()

