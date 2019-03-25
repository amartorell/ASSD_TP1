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


def analogKey(sampleFreq, signalVector, contSignalPeriod, outputSignal):
    auxCounter=1/sampleFreq     #trabajo con periodo
    for x in range(len(signalVector)):
        if(auxCounter<=0):
            outputSignal[x]=0
            auxCounter=1/sampleFreq            
        else:
            outputSignal[x]=signalVector[x]
            auxCounter=auxCounter-contSignalPeriod
            
def sampleAndHold(sampleFreq, signalVector, contSignalPeriod, outputSignal):
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
    
def threeHalfsSine(time,period):

    distance=time[1]-time[0]    #distancia entre valores de la funcion seno. Seria el periodo utilizado para la señal continua
    auxTime=np.arange(time[0],4*time[len(time)-1]+time[0],distance)
    auxSine= np.sin(auxTime*2*np.pi*(1/period))
    timeBase = time[len(time)-1]-time[0]
    amountOfPeriods = timeBase/period
    puntitosPorPeriodo=int(period/distance)  #cantidad de puntitos que entran en un periodo
    #print(puntitosPorPeriodo)
    puntitosPorPeriodoDeTMS=int(puntitosPorPeriodo*(3/2))
    #print(puntitosPorPeriodoDeTMS)
    totalRange = int(puntitosPorPeriodoDeTMS*amountOfPeriods)
    #print(totalRange)
    auxCounter=puntitosPorPeriodoDeTMS
    newFunc = np.zeros(totalRange)                #en este vector ira la amplitud de 3/2 seno, lo hago del doble de largo para que me sorbren lugares
    #revisar
    signChange=-1                             #contador de la cantidad de veces que hay un cambio de positivo a negativo
    state=1
    newFunc[0]=0
    for x in range(1,totalRange):
                
        if( ( (np.sign(auxSine[x-1])!=-1) & (np.sign(auxSine[x])==-1) ) | ( (np.sign(auxSine[x-1])!=1) & (np.sign(auxSine[x])==1) ) ):         #hubo un cambio de signo
            signChange=signChange+1                                          #aumento el contador
            if(signChange%3==0):        #cuando hay dos cambios de signo de + a - tengo que invertir la funcion seno
                state=-state                         #esta variable me indica eso
            

        if(state==1):
            newFunc[x]=-auxSine[x]
        else:
            newFunc[x]=auxSine[x]
            
    newTime=linspace(time[0], time[len(time)-1]*(3/2), len(newFunc))
     
    return newFunc, newTime

f = 1500
periodsShown=7
continuousSampleFreq=20090
continuousPeriod=1/continuousSampleFreq
t = np.linspace(0, periodsShown*(1/f), continuousSampleFreq)
triangle = signal.sawtooth(2 * np.pi * f * t,0.5)
senoFunc = np.sin(t*2*np.pi*f)
#plt.plot(t, senoFunc)

#sampleAndHold(f/15,senoFunc, continuousPeriod, analogKeySignal)

ths, time=threeHalfsSine(t,1/f)
plt.scatter(time,ths)
plt.show()
