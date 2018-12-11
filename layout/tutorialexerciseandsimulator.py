import tkinter as tk
from tutorialtopic import *
from layout.tutorialexercise import *
from layout.tutorialsimulator import *

class TutorialExerciseAndSimulator(TutorialTopic):

    def setOutline(self, outline):
        self.tutText.setOutline(outline)

    def setPrevious(self, previous):
        self.tutText.setPrevious(previous)
        #super().setPrevious(previous)
        #self.buttonPrevious.grid(row=2, column=0, sticky="nsew")

    def setNext(self, next):
        self.tutText.setNext(next)
        #super().setNext(previous)
        #self.buttonNext.grid(row=2, column=2, sticky="nsew")

    #tutorial/actual.should be name.
    #tutorial/actual.tut correspond to file containg tutorial text
    #tutorial/actual.txr corresponds to file containg exercise
    #tutorial/actual.qc contains quantum circuit for simulation
    def __init__(self, parent=None, controller=None, actual=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.grid(row = 0, column = 0, sticky="nsew")
        self.actual = actual;

        self.textFrame = tk.Frame(self, borderwidth=5, bg="orange")
        self.textFrame.grid(row=0, column = 0, sticky="nsew")
        self.tutText = TutorialExercise(parent=self.textFrame,
                controller=self.controller, actual=self.actual)

        self.simFrame = tk.Frame(self, borderwidth=5)
        self.simFrame.grid(row=0, column = 1, sticky="nsew")
        self.tutSim = TutorialSimulator(parent=self.simFrame,
                controller=self.controller, actual=self.actual)
        self.tutSim.buttonPrint()

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        for i in range(2):
            self.columnconfigure(i, weight=1)
