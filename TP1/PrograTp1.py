#!/usr/apps/Python/bin/python
#!/usr/apps/Python/bin/python
import matplotlib, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 

class Main:

        def __init__(self):
            self.root = Tk()
            self.frame = Frame(self.root)
            self.frame.pack()
            self.root.title("ASSD TP1: Entorno de Simulación")
            self.root.resizable(False, False)


            #-----------------------------------
            self.w = Frame (self.root)
            self.w.pack(side=LEFT,fill=BOTH,expand=True,padx=200,pady=200)
            self.w.grid_propagate(0)
            
            SignalList=('3/2 Seno','Cuadratica','Cuadrada','Triangular')
            self.SignalInputString = StringVar()
            self.SignalInputString.set(SignalList[0])
            InputSignalMenu=OptionMenu(self.w,self.SignalInputString,*SignalList)
            InputSignalMenu.grid(row=0,column=1,columnspan=2,padx=5,pady=5)
            InputSignalMenu.pack()
            
            self.Frecuency=Scale(self.w, from_=150, to=15000,resolution=1,label='Frecuency:', orient=HORIZONTAL)
            self.Frecuency.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
            self.Frecuency.pack()
            self.Frecuency.set(1500)
            
            self.Voltage=Scale(self.w, from_=-5, to=5,resolution=0.1,label='Vpp:', orient=HORIZONTAL)
            self.Voltage.grid(row=2,column=1,columnspan=1,padx=5,pady=5)
            self.Voltage.set(5)
            self.Voltage.pack()

            self.DutyCycle=Scale(self.w, from_=5, to=95,resolution=5,label='Duty:', orient=HORIZONTAL)
            self.DutyCycle.grid(row=3,column=1,columnspan=1,padx=5,pady=5)
            self.DutyCycle.pack()
            self.DutyCycle.set(50)
      

            #------------------
            self.root.mainloop()


if __name__ == "__main__":
    ex = Main()