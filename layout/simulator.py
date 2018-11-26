import tkinter as tk
from tkinter import *

"""def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 100):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 100):
        c.create_line([(0, i), (w, i)], tag='grid_line')

root = tk.Tk()

c = tk.Canvas(root, height=1000, width=1000, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)"""

class Simulator(Frame):
    def createHorizontalLines(self, width, height, spacing):
        for i in range(0, height, spacing):
            self.canvas.create_line([(0, i), (width, i)], tag='grid_line')

    def createVerticalLines(self, width, height, spacing):
        for i in range(0, width, spacing):
            self.canvas.create_line([(i, 0), (i, height)], tag='grid_line')

    def createGrid(self):
        self.width = 720
        self.height = 480

        self.canvas = tk.Canvas(self, width=self.width,
                height=self.height, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.createVerticalLines(self.width, self.height, 75)
        self.createHorizontalLines(self.width, self.height, 75)


    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.createGrid()
