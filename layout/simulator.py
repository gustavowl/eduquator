import tkinter as tk
from tkinter import *

class Simulator(Frame):
    def createHorizontalLines(self, width, height, spacing):
        for i in range(0, height, spacing):
            self.canvas.create_line([(0, i), (width, i)], tag='grid_line')

    def createVerticalLines(self, width, height, spacing):
        for i in range(0, width, spacing):
            self.canvas.create_line([(i, 0), (i, height)], tag='grid_line')

    def createGrid(self):
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.grid(sticky="nsew")

        self.createVerticalLines(self.width, self.height, 50)
        self.createHorizontalLines(self.width, self.height, 50)

    def resize(self, event):
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.canvas.delete("grid_line") #delete("all")
        self.createVerticalLines(self.width, self.height, 50)
        self.createHorizontalLines(self.width, self.height, 50)
        

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")

        self.createGrid()

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.bind("<Configure>", self.resize)
