from tkinter import *
from tkinter import ttk

class Sidebar(Frame):

    def createCircuitWidgets(self):
        self.circFr = ttk.Frame(self, borderwidth=5, relief="sunken",
                width=320, height=640)
        #self.scroll = ttk.Scrollbar(self.circFr, orient=VERTICAL) #command =...
        self.circuit_label = ttk.Label(self.circFr, text="Circuit Components")
        self.comp1 = ttk.Button(self.circFr, text="C1") #, width=20
        self.comp2 = ttk.Button(self.circFr, text="C2")
        self.qubit0 = ttk.Button(self.circFr, text="|0⟩")
        self.qubit1 = ttk.Button(self.circFr, text="|1⟩")

        self.circuit_label.grid(row=0, columnspan=2)
        self.comp1.grid(columnspan=2, row=1)
        self.comp2.grid(columnspan=2, row=2, rowspan=2)
        self.qubit0.grid(column=0, row=4)
        self.qubit1.grid(column=1, row=4)
        #self.scroll.grid(column=2, row=0, rowspan=5)

        self.circFr.grid(row=3, columnspan=2)

        for child in self.circFr.winfo_children():
            child.grid_configure(padx=3, pady=3)

    def createActionWidgets(self):
        self.actionFr = ttk.Frame(self, borderwidth=5, relief="sunken",
                width=320, height=640)
        self.simButton = ttk.Button(self.actionFr, text="Start simulation")
        self.tutButton = ttk.Button(self.actionFr, text="Tutorial")

        self.simButton.grid(columnspan=2, row=0)
        self.tutButton.grid(columnspan=2, row=1)

        self.actionFr.grid(row=4, columnspan=2)
        
        for child in self.actionFr.winfo_children():
            child.grid_configure(padx=3, pady=3)

    def createWidgets(self):
        self.fr = ttk.Frame(self, borderwidth=5, relief="sunken",
                width=320, height=640)
        self.tools_label = ttk.Label(self.fr, text="Tools")
        self.button1 = ttk.Button(self.fr, text="1")
        self.button2 = ttk.Button(self.fr, text="2")
        self.button3 = ttk.Button(self.fr, text="3")
        self.button4 = ttk.Button(self.fr, text="4")
        #self.tools_separator = ttk.Separator(self.fr, orient=HORIZONTAL)

        self.fr.grid(column=0, row=0)
        self.tools_label.grid(column=0, row=0, columnspan=2)
        self.button1.grid(column=0, row=1)
        self.button2.grid(column=1, row=1)
        self.button3.grid(column=0, row=2)
        self.button4.grid(column=1, row=2)
        #self.tools_separator.grid(row=3, columnspan=2, sticky=(W, E))

        for child in self.fr.winfo_children():
            child.grid_configure(padx=3, pady=3)

        self.createCircuitWidgets()
        self.createActionWidgets()


    #TODO: Add widgets commands

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.createWidgets()
