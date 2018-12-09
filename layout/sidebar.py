from tkinter import *
from tkinter import ttk

class Sidebar(Frame):

    def createCircuitWidgets(self):
        self.circFr = ttk.Frame(self, borderwidth=5, relief="sunken")
        self.circFr.grid(row=1, column=0, stick="nsew")

        #self.scroll = ttk.Scrollbar(self.circFr, orient=VERTICAL) #command =...
        #self.scroll.grid(column=2, row=0, rowspan=5)

        self.circuit_label = ttk.Label(self.circFr, text="Circuit Components")
        self.circuit_label.grid(row=0, columnspan=2)

        self.comp1 = ttk.Button(self.circFr, text="C1")
        self.comp1.grid(columnspan=2, row=1, sticky="nsew")

        self.comp2 = ttk.Button(self.circFr, text="C2")
        self.comp2.grid(columnspan=2, row=2, rowspan=2, sticky="nsew")

        self.qubit0 = ttk.Button(self.circFr, text="|0⟩")
        self.qubit0.grid(column=0, row=4, sticky="nsew")

        self.qubit1 = ttk.Button(self.circFr, text="|1⟩")
        self.qubit1.grid(column=1, row=4, sticky="nsew")

        for i in range(5):
            self.circFr.rowconfigure(i, weight="1")
        for i in range(2):
            self.circFr.columnconfigure(i, weight="1")

        for child in self.circFr.winfo_children():
            child.grid_configure(padx=3, pady=3)

    def createActionWidgets(self):
        self.actionFr = ttk.Frame(self, borderwidth=5, relief="sunken",
                width=320, height=640)
        self.actionFr.grid(row=2, column=0, sticky="nsew")

        #self.simButton = ttk.Button(self.actionFr, text="Start simulation")
        self.simButton = ttk.Button(self.actionFr, text="Start simulation",
                command=lambda: self.controller.show_frame("ScreenSimulator"))
        self.simButton.grid(columnspan=2, row=0, sticky="nsew")

        self.tutButton = ttk.Button(self.actionFr, text="Tutorial",
                command=lambda: self.controller.show_frame("ScreenTutorial"))
        self.tutButton.grid(columnspan=2, row=1, sticky="nsew")

        for i in range(2):
            self.actionFr.columnconfigure(i, weight=1)
            self.actionFr.rowconfigure(i, weight=1)
        
        for child in self.actionFr.winfo_children():
            child.grid_configure(padx=3, pady=3)

    def createWidgets(self):
        self.toolsFr = ttk.Frame(self, borderwidth=5, relief="sunken")
        self.toolsFr.grid(column=0, row=0, sticky="nsew")
        self.toolsFr.columnconfigure(0, weight=1)
        self.toolsFr.columnconfigure(1, weight=1)
        for i in range(3):
            self.toolsFr.rowconfigure(i, weight=1)


        self.tools_label = ttk.Label(self.toolsFr, text="Tools")
        self.tools_label.grid(column=0, row=0, columnspan=2)

        self.button1 = ttk.Button(self.toolsFr, text="1")
        self.button1.grid(column=0, row=1, sticky="nsew")

        self.button2 = ttk.Button(self.toolsFr, text="2")
        self.button2.grid(column=1, row=1, sticky="nsew")

        self.button3 = ttk.Button(self.toolsFr, text="3")
        self.button3.grid(column=0, row=2, sticky="nsew")

        self.button4 = ttk.Button(self.toolsFr, text="4")
        self.button4.grid(column=1, row=2, sticky="nsew")

        for child in self.toolsFr.winfo_children():
            child.grid_configure(padx=3, pady=3)

        self.createCircuitWidgets()
        self.createActionWidgets()


    #TODO: Add widgets commands

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        self.createWidgets()

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)

        for row in range(3):
            self.rowconfigure(row, weight=1)
