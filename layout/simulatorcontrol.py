from tkinter import *
from tkinter import ttk

class SimulatorControl(Frame):

    def createWidgets(self, onStopPressed):
        self.statusLabel = ttk.Label(self, text="Simulating")
        self.statusLabel.grid(column=1, row=0, columnspan=4)

        self.backButton = ttk.Button(self, text="<<")
        self.backButton.grid(column=1, row=1, sticky="nsew")

        self.pausePlayButton = ttk.Button(self, text="||")
        self.pausePlayButton.grid(column=2, row=1, sticky="nsew")

        self.forwardButton = ttk.Button(self, text=">>")
        self.forwardButton.grid(column=3, row=1, sticky="nsew")

        self.stopButton = ttk.Button(self, text="[]",
                command=lambda: self.controller.show_frame(onStopPressed))
        self.stopButton.grid(column=4, row=1, sticky="nsew")

        for child in self.winfo_children():
            child.grid_configure(padx=3, pady=3)

    def __init__(self, parent, controller, onStopPressed):
        Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(5, weight=3)

        for row in range(4):
            self.rowconfigure(row+1, weight=1)

        self.createWidgets(onStopPressed)
