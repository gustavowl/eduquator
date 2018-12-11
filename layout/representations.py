from tkinter import *
from tkinter import ttk
import tkinter as tk

class Representations(Frame):

    def updateMatrixText(self, text):
        self.matrixText.delete(1.0, tk.END)
        self.matrixText.insert(tk.END, text)

    def updateArrayText(self, text):
        self.arrayText.delete(1.0, tk.END)
        self.arrayText.insert(tk.END, text)

    def createWidgets(self):
        self.representaionsLabel = ttk.Label(self.frame, text="REPRESENTATIONS")
        self.representaionsLabel.grid(column=0, row=0, columnspan=2, sticky="nsew")

        self.matrixText = tk.Text(self.frame)
        self.matrixText.grid(column=0, row=1, sticky="nsew")

        self.arrayText = tk.Text(self.frame)
        self.arrayText.grid(column=1, row=1, sticky="nsew")

        for child in self.winfo_children():
            child.grid_configure(padx=3, pady=3)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(self.parent, borderwidth=5, bg="yellow")
        self.frame.grid(row=0, column=0, sticky="nsew")
        #self.grid(row=0, column=0, sticky="nsew")
        self.createWidgets()

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=2)

        #TODO: SHOW DIFFERENT REPRESENTATIONS
