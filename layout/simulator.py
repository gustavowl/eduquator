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
        self.width = 720
        self.height = 720 #480

        #self.canvas = tk.Canvas(self, width=self.width,
        #        height=self.height, bg="white")
        self.canvas = tk.Canvas(self, bg="white")
        #self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.grid(sticky="nsew")

        self.createVerticalLines(self.width, self.height, 75)
        self.createHorizontalLines(self.width, self.height, 75)


    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.columnconfigure(0, weight=1)
        self.createGrid()
