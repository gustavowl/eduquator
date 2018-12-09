import tkinter as tk
from tutorialtopic import *
from layout.simulator import *

class TutorialSimulator(tk.Frame):

    def __init__(self, parent=None, controller=None, actual=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.grid(row = 0, column = 0, sticky = "nsew")
        self.actual = actual

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #creates simulator grid
        #TODO: load circuit from tutorial/actual.qc
        self.simulatorFrame = tk.Frame(self, borderwidth=5, bg="blue")
        self.simulatorFrame.grid(row = 0, column = 0, sticky = "nsew")

        self.simGrid = Simulator(self.simulatorFrame) #TODO: load circuit
        self.simGrid.grid(row = 0, column = 0, sticky = "nsew")

        self.buttonStartSim = tk.Button(self.simulatorFrame, text = "Start simulation",
                command=lambda: print("TODO SHIFT COMMAND"))
        self.buttonStartSim.grid(row = 1, column = 0, sticky="nsew")
        
        self.simulatorFrame.columnconfigure(0, weight = 1)
        self.simulatorFrame.rowconfigure(0, weight=9)
        self.simulatorFrame.rowconfigure(1, weight=1)
