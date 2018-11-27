from tkinter import *
from tkinter import ttk
from layout.sidebar import *
from layout.simulator import *

class LayoutManager:
    def mainloop(self):
        self.screen.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.title("Eduquator")
        self.root.geometry("1080x720")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)


        self.screen = ttk.Frame(self.root, borderwidth=5, relief="sunken") #,
                #width=320, height=640)
        self.screen.grid(row=0, column=0, sticky="nsew")
        self.screen.rowconfigure(0, weight=1)
        self.screen.columnconfigure(0, weight=1)
        self.screen.columnconfigure(1, weight=4)

        self.sideFrame = tk.Frame(self.screen, borderwidth=5, relief="sunken", bg="red")
        self.sideFrame.grid(row=0, column=0, sticky="nsew")
        self.sb = Sidebar(parent=self.sideFrame)
        #self.sideFrame.columnconfigure(0, weight=1)

        self.simulatorFrame = ttk.Frame(self.screen, borderwidth=5, relief="sunken") #,
                #width=500, height=640)
        self.simulatorFrame.grid(row=0, column=1, sticky="nsew")
        self.simulatorGrid = Simulator(parent=self.simulatorFrame)
