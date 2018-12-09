import tkinter as tk
from tkinter import *
from layout.simulatorcontrol import *
from layout.simulator import *
from layout.representations import *

class ScreenSimulator(Frame):
    
    def __init__(self, parent=None, controller=None):
        Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=9)
        self.rowconfigure(2, weight=9)

        self.simulatorControllerFrame = tk.Frame(self, borderwidth=5, bg="blue")
        self.simulatorControllerFrame.grid(row=0, column=0, sticky="ew")
        self.sc = SimulatorControl(parent=self.simulatorControllerFrame,
                controller=self.controller)
        
        self.simulatorFrame = tk.Frame(self, borderwidth=5, bg="green")
        self.simulatorFrame.grid(row=1, column=0, sticky="nsew")
        self.simulator = Simulator(parent=self.simulatorFrame, controller=self.controller)

        self.repFrame = tk.Frame(self, borderwidth=4, bg="blue")
        self.repFrame.grid(row=2, column=0, sticky="nsew")
        self.representations= Representations(parent=self.repFrame, controller=self.controller)
