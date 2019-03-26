from tkinter import *
import matplotlib, sys
matplotlib.use('TkAgg')
import math
from scipy import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.pyplot import plot,xscale,show
import matplotlib.patches as patches
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib, sys
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from tkinter import messagebox
from scipy import signal


#root = Tk()

class TP1:

    def __init__(self):
        self.root = Tk()
        self.root.title("ASSD: Entorno de Simulacion")
        self.root.resizable(False,False)
        self.ventana_izquierda = Frame(self.root)
        self.ventana_izquierda.grid()

        self.ventana_derecha = Frame(self.root)
        self.ventana_derecha.grid(row=0,column=1)
        self.label_test = Label(self.ventana_derecha,text="probando")
        self.label_test.grid()

        self.ventana_inferior = Frame(self.root)
        self.ventana_inferior.grid(row=1)


        self.label_1 = Label(self.ventana_derecha,text="Caracteristicas de la señal:")
        self.label_1.grid(row=0,column=0,columnspan=4)

        self.label_2 = Label(self.ventana_derecha,text="Aca no se que poner")
        self.label_2.grid(row=5,column=0)

        SignalList = ('Sin', 'Triangular', '3/2 Sin')
        self.SignalInputString = StringVar()
        self.SignalInputString.set(SignalList[0])
        InputSignalMenu = OptionMenu(self.ventana_derecha, self.SignalInputString, *SignalList)
        InputSignalMenu.grid(row=1, column=0)

        self.Frecuency = Scale(self.ventana_derecha, from_=150, to=17000, resolution=1, label='Frecuency:', orient=HORIZONTAL)
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
        self.CheckFAA.grid(row=6,column=0,columnspan=2,padx=8,pady=8)

        self.check_sample_and_hold = IntVar()
        self.CheckSAH = Checkbutton(self.ventana_derecha, text="Sample and Hold", variable=self.check_sample_and_hold)
        self.CheckSAH.grid(row=7,column=0,columnspan=2,padx=8,pady=8)

        self.check_llave_analog = IntVar()
        self.CheckANKEY = Checkbutton(self.ventana_derecha, text="Llave analogica", variable=self.check_llave_analog)
        self.CheckANKEY.grid(row=8,column=0,columnspan=2,padx=8,pady=8)

        self.check_fr = IntVar()
        self.CheckFR = Checkbutton(self.ventana_derecha, text="FR", variable=self.check_fr)
        self.CheckFR.grid(row=9,column=0,columnspan=2,padx=8,pady=8)

        self.GraphButtom = Button(self.ventana_derecha, text="Graficar", command=self.Graficar)
        self.GraphButtom.grid(row=10,column=0,columnspan=2)



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
        a,r,H = self.SetEntry()
        
        #-----plot-------
        self.axis.clear()
        self.axis.clear()
        self.axis.set_title('TP1 ASSD')
        self.axis.set_aspect('auto',adjustable='box')
        self.axis.plot(a,r)
        self.dataPlot.draw()
        
    
    def SetEntry(self):
        N = 100000 #numero de sampleo
        print("Numero de Sampleo o Continua Segun tomi = ",N)    # sample spacing
        f = self.Frecuency.get() #mi frecuencia
        print(f)
        T = 1.0 / (1000*f) #Por cada senoidal q meto me toma 100 puntos por frecuencia, es decir muestrea 10 veces mas rapido q la señal siempre
        t = np.linspace(0.0, N*T, N) #toma N puntos entre (0; N/10f)

        FrecuenciaLLA = 60000
        FSnH = 170
                                                ###---ACA DEFINO TODAS MIS FUNCIONES---####

        y = np.sin(f * 2.0*np.pi*t)

        #tresmediosdeseno[i] = math.sin(f*2*np.pi*i/T)
        #triangular 
                                                ###---ACA DEFINO TODOS MIS MODULOS---###

        #FAA
        H = signal.TransferFunction([1],[1/(100*2*np.pi),1])
        
        if(self.check_faa.get() & (self.check_sample_and_hold.get()==0) & (self.check_llave_analog.get()==0) & (self.check_fr.get()==0) ):
            t,y = self.FFA(H,y,t)
            print("primer if1")
            
        if((self.check_faa.get()==0) & (self.check_sample_and_hold.get()) & (self.check_llave_analog.get()==0) & (self.check_fr.get()==0) ):
           y =  self.sampleAndHold(FSnH,y,N)
           print("primer if2")


        if((self.check_faa.get()==0) & (self.check_sample_and_hold.get()==0) & (self.check_llave_analog.get()) & (self.check_fr.get()==0) ):
            y = self.analogKey(FrecuenciaLLA,y,N)  
            print("primer if3")
  
        print("primer noif")

        
        return t,y,H 
           

    #AnalogKey
    def analogKey(self,sampleFreq, signalVector, contSignalPeriod):
        auxCounter=1/sampleFreq     #trabajo con periodo
        outputSignal = signalVector
        for x in range(len(signalVector)):
            if(auxCounter<=0):
                outputSignal[x]=0
                auxCounter=1/sampleFreq            
            else:
                outputSignal[x]=signalVector[x]
                auxCounter=auxCounter-contSignalPeriod
            return outputSignal 

    #Sample&Hold
    def sampleAndHold(self,sampleFreq, signalVector, contSignalPeriod):
        outputSignal = signalVector
        auxCounter=1/sampleFreq
        holdValue=signalVector[0]
        for x in range(len(signalVector)):
            if(auxCounter<=0):
                holdValue=signalVector[x]
                outputSignal[x]=holdValue
                auxCounter=1/sampleFreq            
            else:
                outputSignal[x]=holdValue
                auxCounter=auxCounter-contSignalPeriod
        return outputSignal
        #ploteo de funcion en tiempo
    def PlotInTime(self,t,y,Legend, tipo):
        if(tipo==0):
            plt.plot(t,y)
            plt.legend(Legend)
            plt.grid()
            plt.show()
        elif (tipo==1):
            plt.scatter(t,y)
            plt.legend(Legend)
            plt.grid()
            plt.show()
        else:
            pass    

    def PlotInFrecuency(self,N,T,y,Legend):
        yfb = fft(y)
        fb = np.linspace(0.0, 1.0/(2.0*T), N/2) #recorto por dos mi vector de frecuencias porque solo voy a estar con las positivas
        plt.semilogx(fb[1:N//2], 2.0/N * np.abs(yfb[1:N//2]), '-b')
        plt.legend(Legend)
        plt.grid()
        plt.show()


    #Filtro FFA
    def FFA(self,H,y,t):
        (T2,YAfterFilter,x2) = signal.lsim(H, y, t, X0=0, interp=1)
        YAfterFilter = YAfterFilter[(int) (len(YAfterFilter)/1.1):] #recorte para ver de sacar mi transitorio que se me arma de que mi señal no viene desde menos inf
        T2= T2[(int) (len(T2)/1.1):]
        return T2, YAfterFilter        



if __name__ == "__main__":
    ex = TP1()

