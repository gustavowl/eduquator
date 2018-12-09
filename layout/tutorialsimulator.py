import tkinter as tk
from tutorialtopic import *
from layout.simulator import *
from layout.screensimulator import *

class TutorialSimulator(tk.Frame):

    def show_frame(self, frame):
        #assert frame \in tk.Frame
        frame.tkraise()

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
        self.simulatorFrame = tk.Frame(self, borderwidth=5, bg="purple")
        self.simulatorFrame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.simulatingFrame = tk.Frame(self, borderwidth=5, bg="purple")
        self.simulatingFrame.grid(row = 0, column = 0, sticky = "nsew")

        #TODO: load circuit from tutorial/actual.qc
        self.simGrid = Simulator(self.simulatorFrame) #TODO: load circuit
        self.simGrid.grid(row = 0, column = 0, sticky = "nsew")

        self.buttonStartSim = tk.Button(self.simulatorFrame, text = "Start simulation",
                command=lambda: self.show_frame(self.simulatingFrame))
        self.buttonStartSim.grid(row = 1, column = 0, sticky="nsew")
        
        self.simulatorFrame.columnconfigure(0, weight = 1)
        self.simulatorFrame.rowconfigure(0, weight=9)
        self.simulatorFrame.rowconfigure(1, weight=1)

        #creates simulating
        self.screenSim = ScreenSimulator(parent=self.simulatingFrame,
                controller = self.controller, onStopPressed = self.simulatorFrame)
        self.screenSim.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(self.simulatorFrame)
