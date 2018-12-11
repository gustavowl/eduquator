import tkinter as tk
from tutorialtopic import *
from layout.simulator import *
from layout.screensimulator import *

class TutorialSimulator(tk.Frame):

    def start_simulation(self):
        self.show_frame(self.simulatingFrame)

    def buttonSimulation(self):
        #self.buttonPrint = None
        self.buttonStartSim = tk.Button(self.simulatorFrame, text = "Start simulation",
                command=self.start_simulation)
        self.buttonStartSim.grid(row = 1, column = 0, sticky="nsew")

    def print_circuit(self):
        print("TODO: PRINT CIRCUIT\n")

    def buttonPrint(self):
        #self.buttonStartSim = None
        self.buttonPrint = tk.Button(self.simulatorFrame, text = "Print circuit",
                command=self.print_circuit)
        self.buttonPrint.grid(row = 1, column = 0, sticky="nsew")

    def show_frame(self, frame):
        #assert frame \in tk.Frame
        frame.tkraise()

    def enable_simulation(self, enabled):
        self.simulationEnabled = enabled

    def __init__(self, parent=None, controller=None, actual=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.grid(row = 0, column = 0, sticky = "nsew")
        self.actual = actual.strip()

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.enable_simulation(True)

        #creates simulator grid
        self.simulatorFrame = tk.Frame(self, borderwidth=5, bg="purple")
        self.simulatorFrame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.simulatingFrame = tk.Frame(self, borderwidth=5, bg="purple")
        self.simulatingFrame.grid(row = 0, column = 0, sticky = "nsew")

        self.simGrid = Simulator(self.simulatorFrame) 
        self.simGrid.grid(row = 0, column = 0, sticky = "nsew")
        self.simGrid.loadCircuit(self.actual)
        self.simGrid.drawCircuit()
        
        self.simulatorFrame.columnconfigure(0, weight = 1)
        self.simulatorFrame.rowconfigure(0, weight=9)
        self.simulatorFrame.rowconfigure(1, weight=1)

        self.buttonSimulation()

        #creates simulating
        self.screenSim = ScreenSimulator(parent=self.simulatingFrame,
                controller = self.controller, onStopPressed = self.simulatorFrame)
        self.screenSim.grid(row = 0, column = 0, sticky = "nsew")
        self.screenSim.setCircuit(self.actual)

        self.show_frame(self.simulatorFrame)
