from scipy import*
import numpy as np
import matplotlib.pyplot as plt
import matplotlib, sys
matplotlib.use('TkAgg')
from scipy import signal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

N = 100000 #numero de sampleo
# sample spacing
f = 1500 #mi frecuencia
T = 1.0 / (100*f) #Por cada senoidal q meto me toma 100 puntos por frecuencia, es decir muestrea 10 veces mas rapido q la señal siempre
t = np.linspace(0.0, N*T, N) #toma N puntos entre (0; N/10f)
FrecuenciaLLA = 1700
FSnH = 1700
                                        ###---ACA DEFINO TODAS MIS FUNCIONES---####

y = np.sin(f * 2.0*np.pi*t)

#tresmediosdeseno[i] = math.sin(f*2*np.pi*i/T)
#triangular 
                                        ###---ACA DEFINO TODOS MIS MODULOS---###

#FAA
H = signal.TransferFunction([1],[1/(100*2*np.pi),1])

#AnalogKey
def analogKey(sampleFreq, signalVector, contSignalPeriod):
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

# Sample&Hold
def sampleAndHold(sampleFreq, signalVector, contSignalPeriod):
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
    return outputSignal                                 #deberia tener las mismas dimenciones que signalVector
                                    ###---CODIGO----#

#ploteo de funcion en tiempo
def PlotInTime(t,y,Legend, tipo):
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

#ploteo de funcion en frecuencia
def PlotInFrecuency(N,T,y,Legend):
    yfb = fft(y)
    fb = np.linspace(0.0, 1.0/(2.0*T), N/2) #recorto por dos mi vector de frecuencias porque solo voy a estar con las positivas
    plt.semilogx(fb[1:N//2], 2.0/N * np.abs(yfb[1:N//2]), '-b')
    plt.legend(Legend)
    plt.grid()
    plt.show()


#Filtro FFA
def FFA(H,y,t):
    (T2,YAfterFilter,x2) = signal.lsim(H, y, t, X0=0, interp=1)
    YAfterFilter = YAfterFilter[(int) (len(YAfterFilter)/2):] #recorte para ver de sacar mi transitorio que se me arma de que mi señal no viene desde menos inf
    T2= T2[(int) (len(T2)/2):]
    return T2, YAfterFilter 



PlotInTime(t,y,"Entrada en Tiempo",0)

PlotInFrecuency(N,T,y,"Entrada en Frecuencia")

#Entro a FFA
t2, y2 = FFA(H,y,t)

PlotInTime(t2,y2,"Salida del Filtro en Tiempo",0)

PlotInFrecuency((int) (N/2) ,T,y2,"Salida del Filtro en Frecuencia")

#Entro a S&H

y3 = sampleAndHold(FSnH,y2,1/(N/2)) #OJO Q y1 esta asociado a N y t, e y2 esta asociado a N/2 y t2

PlotInTime(t2,y3,"Salida del S&H en Tiempo",1) 

PlotInFrecuency((int) (N/2),T,y3,"Salida del S&H en Frecuencia") 


#Entro a Llave Analógica

y4= analogKey(FrecuenciaLLA,y3,N/2)

PlotInTime(t2,y4,"Salida de la analog en Tiempo",1) 

PlotInFrecuency((int) (N/2) ,T,y4,"Salida de la analog en Frecuencia") 

#Entro al filtro Recuperador



"""
p = YbeforeFilter
sampleAndHold(60000,YbeforeFilter,1/N,p)
plt.scatter(x,p)
plt.grid()
plt.show()

z = YbeforeFilter
analogKey(1000,YbeforeFilter,N,z)
plt.scatter(x,z)
plt.grid()
plt.show()

#ploteo funcion despues del filtro en tiempo
plt.plot(T2,YAfterFilter)
plt.show()

#ploteo funcion despues del filtro en frecuencia
yfa = fft(YAfterFilter)
fa = np.linspace(0.0,1.0/(2*T),N/4)    #recorto por cuatro N porque mi vector tuvo otro recorte a la mitad por el transitorio
plt.plot(fa[1:N//4], 2.0/N * np.abs(yfa[1:N//4]), '-r')
#plt.semilogy(xf[1:N//2], 2.0/N * np.abs(ywf[1:N//2]), '-r')
plt.legend(['FFT Señal Después del Filtro'])
plt.grid()
plt.show()
"""