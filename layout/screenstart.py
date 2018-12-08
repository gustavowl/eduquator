from tkinter import *
from tkinter import ttk
from layout.sidebar import *
from layout.simulator import *

class ScreenStart(Frame):

    def __init__(self, parent=None, controller=None):
        Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row = 0, column=0, sticky="nsew")

        #parent.columnconfigure(0, weight=1)
        #parent.rowconfigure(0, weight=1)

        #self.startScreen = ttk.Frame(self.root, borderwidth=5, relief="sunken")
        #self.startScreen.grid(row=0, column=0, sticky="nsew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
       
        self.sideFrame = tk.Frame(self, borderwidth=5, relief="sunken", bg="red")
        self.sideFrame.grid(row=0, column=0, sticky="nsew")
        self.sb = Sidebar(parent=self.sideFrame, controller=self.controller)

        self.simulatorFrame = tk.Frame(self, borderwidth=5, relief="sunken", bg="orange")
        self.simulatorFrame.grid(row=0, column=1, sticky="nsew")
        self.simulatorGrid = Simulator(parent=self.simulatorFrame, controller=self.controller)
