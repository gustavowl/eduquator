import tkinter as tk
from tutorialtopic import *

class TutorialText(TutorialTopic):

    def summon(self, event):
        index = self.labels.index(event.widget)
        self.controller.show_frame(self.tutorialTopics[index])

    #tutorial/actual.should be name.
    #tutorial/actual.tut correspond to file containg tutorial text
    #tutorial/actual.txr corresponds to file containg exercise
    #tutorial/actual.qc contains quantum circuit for simulation
    def __init__(self, parent=None, controller=None, actual=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row = 0, column = 0, sticky="nsew")
        self.actual = actual;

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.labels = []

        #creates Tutorial main label
        self.mainLabel = tk.Label(self, text=self.actual)
        self.mainLabel.grid(row=0, column=1, sticky="nsew")

        #creates tutorial text
        #TODO: read text from actual.tut file
        self.text = tk.Text(self)
        self.text.grid(row=1, columnspan=3, sticky="nsew")
        self.text.insert(tk.END, "TODO: READ TUTORIAL TEXT FILE\n\n" +
                "PREIFHPQWOIEHFPDFJA\nPWFEPDUGFPA\nPOAUGDSPF")

        #creates "quit button"
        self.quit = tk.Button(self, text="Quit", command=lambda:
                self.controller.show_frame(self.outline))
        self.quit.grid(row=2, column=1, sticky="nsew")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.rowconfigure(2, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)
