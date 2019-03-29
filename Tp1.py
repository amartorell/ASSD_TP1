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

        self.ventana_inferior = Frame(self.root)
        self.ventana_inferior.grid(row=1)


        self.label_1 = Label(self.ventana_derecha,text="Caracteristicas de la señal:")
        self.label_1.grid(row=0,column=2,columnspan=2, sticky=W)

        self.label_2 = Label(self.ventana_derecha,text="Aca no se que poner")
        self.label_2.grid(row=5,column=0)

        self.label_3 = Label(self.ventana_derecha, text='Que ver:')
        self.label_3.grid(row=1, column=5, sticky=W)

        SignalList = ('Seno', '3/2 Seno','Triangular')
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

        self.Frecuencia_SH=Scale(self.ventana_derecha, from_=1500, to=100000, label='Frecuencia S&h', orient=HORIZONTAL)
        self.Frecuencia_SH.set(30000)

        self.Duty_SH=Scale(self.ventana_derecha, from_=5, to=95, label='Duty cycle S&H', orient=HORIZONTAL)
        self.Duty_SH.set(50)

        self.check_llave_analog = IntVar()
        self.CheckANKEY = Checkbutton(self.ventana_derecha, text="Llave analogica", variable=self.check_llave_analog, command=self.mostrar_config_LLA)
        self.CheckANKEY.grid(row=6,column=4,columnspan=2,padx=8,pady=8)

        self.frecuencia_LLA = Scale(self.ventana_derecha, from_=1500, to=100000, label='Frecuencia', orient=HORIZONTAL)
        self.frecuencia_LLA.set(3000)

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
        t,y,NuevoN,T = self.SetEntry()
         #-----plot-------Decidir si frecuencia o en tiempo. set entry me devuelve datos para ambos
        if(self.check_frec_graficar.get()==0):
            self.PlotInTime(t,y,0)
            
        if(self.check_tiempo_graficar.get()==0):
            self.PlotInFrecuency(NuevoN,T,y)  
        
    
    def SetEntry(self):
        N = 100000 #numero de sampleo
        print("Numero de Sampleo o Continua Segun tomi = ",N)    # sample spacing
        f = self.Frecuency.get() #mi frecuencia
        print(f)
        T = 1.0 / (1000*f) #Por cada senoidal q meto me toma 1000 puntos por frecuencia, es decir muestrea 10 veces mas rapido q la señal siempre
        t = np.linspace(0.0, N*T, N*10) #toma N puntos entre (0; N/1000f)
        distanceBetweenSamples=t[1]-t[0]

        FrecuenciaLLA = self.frecuencia_LLA.get()
        FSnH = self.Frecuencia_SH.get()
        print("frecuencia de la llave ", FrecuenciaLLA)
        print("frecuencia de snh ", FSnH)
                                                ###---ACA DEFINO TODAS MIS FUNCIONES---####
        y = np.sin(f * 2.0*np.pi*t)
        y = y*self.Voltage.get()

        #tresmediosdeseno[i] = math.sin(f*2*np.pi*i/T)
        #triangular 
                                                ###---ACA DEFINO TODOS MIS MODULOS---###

        #FAA
        H = signal.TransferFunction([1],[1/(100*2*np.pi),1])
        
        if(self.check_faa.get()):
            t,y = self.FFA(H,y,t) #FFA me divide el vector 1.1
            if(self.check_frec_graficar.get()==0):
                y = y[(int) (len(y)/1.1):] #recorte para ver de sacar mi transitorio que se me arma de que mi señal no viene desde menos inf
                t= t[(int) (len(T2)/1.1):]
            
            print("1")

        if(self.check_sample_and_hold.get()):
           y = self.sampleAndHold(FSnH,y,distanceBetweenSamples)
           if(self.check_frec_graficar.get()==0):
                y = y[(int) (len(y)/1.5):] #recorte para ver de sacar mi transitorio que se me arma de que mi señal no viene desde menos inf
                t = t[(int) (len(t)/1.5):]
           
           print("2")

        if(self.check_llave_analog.get()):
           y = self.analogKey(FrecuenciaLLA,y,distanceBetweenSamples,self.duty_cycle_LLA.get()/100)
           print("3")
           print(self.duty_cycle_LLA.get()/100)
           if(self.check_frec_graficar.get()==0):
                y = y[(int) (len(y)/1.5):] #recorte para ver de sacar mi transitorio que se me arma de que mi señal no viene desde menos inf
                t = t[(int) (len(t)/1.5):]
           

        
        if(self.check_fr.get()):
           t,y = self.FFR(H,y,t)
           if(self.check_frec_graficar.get()==0):
                y = y[(int) (len(y)/2):] #recorte para ver de sacar mi transitorio que se me arma de que mi señal no viene desde menos inf
                t= t[(int) (len(t)/2):]
           
           print("4")


        return t,y,(int) (len(y)/10),T
           

    #AnalogKey
    def analogKey(self,sampleFreq, signalVector, distance, dutyCycle):
        auxCounter=1/sampleFreq     #trabajo con periodo
        outputSignal = signalVector
        openKeyCondition=auxCounter*dutyCycle
        #bottomLimit=auxCounter-topLimit
        for x in range(len(signalVector)):
            if(auxCounter>=openKeyCondition):
                outputSignal[x]=signalVector[x]
                auxCounter=auxCounter-distance    
            else:
                if(auxCounter<=0):
                    auxCounter=1/sampleFreq         #reseteo el periodo
                outputSignal[x]=0
                auxCounter=auxCounter-distance

                
        return outputSignal 

    #Sample&Hold
    def sampleAndHold(self,sampleFreq, signalVector, distance):
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
                auxCounter=auxCounter-distance
        return outputSignal
        #ploteo de funcion en tiempo
    def PlotInTime(self,t,y,tipo):
        if(tipo==0):
            self.axis.clear()
            self.axis.set_title('TP1 ASSD')
            self.axis.set_aspect('auto',adjustable='box')
            self.axis.plot(t,y)
            self.dataPlot.draw()
        elif (tipo==1):
            plt.scatter(t,y)
        else:
            pass    

    def PlotInFrecuency(self,N,T,y):
        self.axis.clear()
        self.axis.set_title('TP1 ASSD')
        self.axis.set_aspect('auto',adjustable='box')

        yfb = fft(y)
        fb = np.linspace(0.0, 1/(2.0*T), N/2) #recorto por dos mi vector de frecuencias porque solo voy a estar con las positivas
        self.axis.loglog(fb[1:N//2], 2.0/N * np.abs(yfb[1:N//2]), '-b')
        self.dataPlot.draw()


    #Filtro FFA
    def FFA(self,H,y,t):
        (T2,YAfterFilter,x2) = signal.lsim(H, y, t, X0=0, interp=1)
        return T2, YAfterFilter        

    def FFR(self,H,y,t):
        (T2,YAfterFilter,x2) = signal.lsim(H, y, t, X0=0, interp=1)
        return T2, YAfterFilter        
 
    
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


if __name__ == "__main__":
    ex = TP1()