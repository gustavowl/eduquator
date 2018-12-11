import tkinter as tk
from tkinter import *
from layout.simulatorcontrol import *
from layout.simulator import *
from layout.representations import *

class ScreenSimulator(Frame):

    def updateRepresentation(self, matrix, array):
        if (matrix == None):
            matrix = ""
        if (array == None):
            array = ""
        self.representations.updateMatrixText(matrix)
        self.representations.updateArrayText(array)
    
    def setCircuit(self, circuit):
        self.simulator.loadCircuit(circuit)
        self.simulator.drawCircuit()

    def __init__(self, parent=None, controller=None, onStopPressed=None):
        Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=9)
        self.rowconfigure(2, weight=9)
        
        self.simulatorFrame = tk.Frame(self, borderwidth=5, bg="green")
        self.simulatorFrame.grid(row=1, column=0, sticky="nsew")
        self.simulator = Simulator(parent=self.simulatorFrame, controller=self)

        self.simulatorControllerFrame = tk.Frame(self, borderwidth=5, bg="blue")
        self.simulatorControllerFrame.grid(row=0, column=0, sticky="ew")
        self.sc = SimulatorControl(parent=self.simulatorControllerFrame,
                controller=self.controller, onStopPressed=onStopPressed,
                underControl=self.simulator)

        self.repFrame = tk.Frame(self, borderwidth=4, bg="blue")
        self.repFrame.grid(row=2, column=0, sticky="nsew")
        self.representations = Representations(parent=self.repFrame, controller=self.controller)

        self.simulator.drawCircuit()
