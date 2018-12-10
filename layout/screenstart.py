from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from layout.sidebar import *
from layout.simulator import *

class ScreenStart(Frame):

    def selectCircuitFile(self):
        self.filename =  filedialog.askopenfilename(initialdir = "/home/",
                title = "Select file",
                filetypes = (("quantum circuit files","*.qc"),("all files","*.*")))
        self.circuitInWorkspace = self.filename
        self.simulatorGrid.loadCircuit(self.circuitInWorkspace)
        self.simulatorGrid.drawCircuit()

    def getCircuit(self):
        return self.circuitInWorkspace

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

        #https://www.tutorialspoint.com/python/tk_menu.htm
        self.menubar = Menu(parent)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open", command=self.selectCircuitFile)
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save as...")
        filemenu.add_command(label="Close")

        self.menubar.add_cascade(label="File", menu=filemenu)
       
        self.sideFrame = tk.Frame(self, borderwidth=5, relief="sunken", bg="red")
        self.sideFrame.grid(row=0, column=0, sticky="nsew")
        self.sb = Sidebar(parent=self.sideFrame, controller=self.controller)

        self.simulatorFrame = tk.Frame(self, borderwidth=5, relief="sunken", bg="orange")
        self.simulatorFrame.grid(row=0, column=1, sticky="nsew")
        self.simulatorGrid = Simulator(parent=self.simulatorFrame, controller=self.controller)
        
        self.circuitInWorkspace = None
        self.simulatorGrid.drawCircuit()

        parent.config(menu=self.menubar)
