from tkinter import *
from tkinter import ttk

class Representations(Frame):

    def createWidgets(self):
        self.representaionsLabel = ttk.Label(self, text="REPRESENTATIONS")
        self.representaionsLabel.grid(column=0, row=0)

        for child in self.winfo_children():
            child.grid_configure(padx=3, pady=3)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        self.createWidgets()

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #TODO: SHOW DIFFERENT REPRESENTATIONS
