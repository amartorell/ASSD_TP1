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

#Creo mi funcion de FAA
H = signal.TransferFunction([1],[1/(100*2*np.pi),1])

#Creo mi arreglo de senoidal y tiempo
f = 10000
xx = np.arange(0, 100/f ,1/(f*100))
yy = np.sin(xx*2*np.pi*f)

#Creo mi arreglo de Triangular y tiempo

#Devuelvo mi arreglo modificado por mi filtro
(T,y,x) = signal.lsim(H, yy, xx, X0=0, interp=1)

#Ploteo mi señal modificada
y = y[(int) (len(y)/2):] #recorte para ver de sacar mi transitorio que se me arma de que mi señal no viene desde menos inf
T= T[(int) (len(T)/2):]  #al ingresar a signal.lsim por esto mi nuevo vector busco que quede en el transitorio.
plt.plot(T, y)           #Esta forma de hacerlo anda joya de 100hz a 10000hz ya dsps el vector me queda en el trans   
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()



w, mag, phase = signal.bode(H)

# Plot the data
plt.semilogx(w, mag, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()





