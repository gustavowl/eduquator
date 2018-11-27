from tkinter import *
from tkinter import ttk
from layout.sidebar import *
from layout.simulator import *

class LayoutManager:
    def mainloop(self):
        self.screen.mainloop()

    def __init__(self):
        self.root = Tk()
        self.screen = ttk.Frame(self.root, borderwidth=5, relief="sunken",
                width=320, height=640)

        self.sideFrame = ttk.Frame(self.screen, borderwidth=5, relief="sunken",
                width=320, height=640)
        self.sb = Sidebar(parent=self.sideFrame)
        self.sideFrame.grid(row=0, column=0)
        self.screen.rowconfigure(0, weight=1)

        self.simulatorFrame = ttk.Frame(self.root, borderwidth=5, relief="sunken",
                width=500, height=640)
        self.simulatorGrid = Simulator(parent=self.simulatorFrame)
        self.simulatorFrame.grid(row=0, column=1)

        self.screen.grid(row=0, column=0)
