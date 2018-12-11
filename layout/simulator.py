import tkinter as tk
from tkinter import *
from filemanager import *

class Simulator(Frame):
    def loadCircuit(self, filename):
        self.quantumCircuit = self.fileManager.readQuantumCircuit(filename)

    def drawCircuit(self):
        if (self.quantumCircuit != None):
            qcmatrix = self.quantumCircuit.getCircuit()
            for y in range (len(qcmatrix)):
                for x in range (len(qcmatrix[y])):
                    self.canvas.create_text(self.spacing / 2 + x * self.spacing,
                            self.spacing / 2 + y * self.spacing, font="Times 18 bold",
                            text=qcmatrix[y][x].getLabel())

            self.quantumCircuit.print()

    def erasePlayLine(self):
        self.canvas.delete("play_line")

    def drawPlayLine(self, x):
        self.canvas.delete("play_line")
        qc = self.quantumCircuit.getCircuit()
        y = len(qc)
        for i in range (self.play_line_thickness):
            self.canvas.create_line( [(x + i, 0), (x + i, y * self.spacing)],
                tag="play_line" )

        return len(qc[0]) * self.spacing <= x

    def getNextOperator(self, x, qc):
        if (x <= 0 or x >= len(qc[0])):
            return np.matrix("")
        operator = qc[0][x].getMatrix()
        for i in range (1, len(qc)):
            operator = np.kron(operator, qc[i][x].getMatrix())

        return operator 

    def updateRepresentation(self, x):
        #if previous state is initial, then reset
        qc = self.quantumCircuit.getCircuit()
        y = len(qc)
        update = False
        if (x - 1 == 0):
            self.state = qc[0][0].getVec()
            self.operator = np.matrix("")

            for i in range(1, y):
                self.state = np.kron(self.state, qc[i][0].getVec())

            update = True
        elif ((x + self.play_line_thickness) % self.spacing == 0):
            xcircuit = int((x + self.play_line_thickness) / self.spacing)
            if (self.operator.any()):
                #apply operator
                self.state = self.operator * self.state

            self.operator = self.getNextOperator(xcircuit, qc)

            update = True

                
        if update:
            self.controller.updateRepresentation(str(self.operator), str(self.state))

    def createHorizontalLines(self, width, height, spacing):
        for i in range(0, height, spacing):
            self.canvas.create_line([(0, i), (width, i)], tag='grid_line')

    def createVerticalLines(self, width, height, spacing):
        for i in range(0, width, spacing):
            self.canvas.create_line([(i, 0), (i, height)], tag='grid_line')

    def createGrid(self):
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.spacing = 125

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.grid(sticky="nsew")

        self.createVerticalLines(self.width, self.height, self.spacing)
        self.createHorizontalLines(self.width, self.height, self.spacing)

    def resize(self, event):
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self.canvas.delete("grid_line") #delete("all")
        self.createVerticalLines(self.width, self.height, self.spacing)
        self.createHorizontalLines(self.width, self.height, self.spacing)

    def setClickable(self, c):
        self.clickable = c

    def clicked(self, event):
        if (self.quantumCircuit != None):
            qc = self.quantumCircuit.getCircuit()
            if (event.x <= len(qc[0]) * self.spacing and
                    event.y <= len(qc) * self.spacing):

                x = int(event.x / self.spacing)
                y = int(event.y / self.spacing)
                self.controller.clicked(qc[y][x].getLabel())
        
    def __init__(self, parent=None, controller=None):
        Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.createGrid()
        self.canvas.bind("<Button-1>", self.clicked)
        self.clickable = False

        self.bind("<Configure>", self.resize)

        self.quantumCircuit = None
        self.fileManager = FileManager()

        self.play_line_thickness = 5

        self.drawCircuit()
