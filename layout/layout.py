from tkinter import *
from tkinter import ttk
from layout.sidebar import *

class LayoutManager:
    def mainloop(self):
        #TODO: SHOW CANVAS GRID
        print("TODO: SHOW CANVAS GRID")
        self.screen.mainloop()

    def __init__(self):
        self.root = Tk()
        self.screen = ttk.Frame(self.root, borderwidth=5, relief="sunken",
                width=320, height=640)

        self.sideFrame = ttk.Frame(self.screen, borderwidth=5, relief="sunken",
                width=320, height=640)
        self.sb = Sidebar(parent=self.sideFrame)
        self.sideFrame.grid(row=0, column=0)

        self.simulatorGrid = ttk.Frame(self.root, borderwidth=5, relief="sunken",
                width=500, height=640)
        self.sb2 = Sidebar(parent=self.simulatorGrid)
        self.simulatorGrid.grid(row=0, column=1)

        self.screen.grid(row=0, column=0)
