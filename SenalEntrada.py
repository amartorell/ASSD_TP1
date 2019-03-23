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


f = 1500
periodsShown=2
continuousSampleFreq=100000
continuousPeriod=1/continuousSampleFreq
t = np.linspace(0, periodsShown*(1/f), continuousSampleFreq)
triangle = signal.sawtooth(2 * np.pi * f * t,0.5)
senoFunc = np.sin(t*2*np.pi*f)
#plt.plot(t, senoFunc)


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
    

        
analogKeySignal = triangle
sampleAndHold(f/15,triangle, continuousPeriod, analogKeySignal)

plt.scatter(t,analogKeySignal)
plt.show()