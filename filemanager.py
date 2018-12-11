from quantumcircuit import *
from qubit import *
from quantumgate import *

class FileManager:

    def createQubit(self, label):
        print("circuit read from file. Label: " + label)
        qubit = Qubit()
        if (label == "0"):
            qubit.set0()
        elif (label == "1"):
            qubit.set1()
        elif (label == "+"):
            qubit.setPlus()
        elif (label == "-"):
            qubit.setMinus()
        else:
            return None

        return qubit

    def createQuantumGate(self, label):
        gate = QuantumGate()
        if (label == "X"):
            gate.setXgate()
        elif (label == "Y"):
            gate.setYgate()
        elif (label == "Z"):
            gate.setZgate()
        elif (label == "I"):
            gate.setIdentity()
        elif (label == "H"):
            gate.setHadamard()
        elif (label == "CNOT"):
            print("TODO READ CNOT GATE FROM CIRCUIT FILE")
            return None
        else:
            return None

        return gate

    def readQuantumCircuit(self, filename):
        if (filename == "" or filename == None):
            return None

        if (filename[-3:] == ".qc"):
            self.file = open(filename, "r")
        else:
            self.file = open("circuits/" + filename + ".qc", "r")

        #create new QC
        qc = QuantumCircuit()
        text = self.file.read()
        lines = text.split("\n")
        for y in range(len(lines) - 1):
            cells = lines[y].split(",")
            for x in range(len(cells)):
                if (x != 0):
                    gate = self.createQuantumGate(cells[x])
                    if (gate == None):
                        print("Error while reading quantum gate from circuit file")
                        self.file.close()
                        self.file = None
                        return None
                    qc.addGate(gate, x, y)
                else:
                    qubit = self.createQubit(cells[x])
                    if (qubit == None):
                        print("Error while reading qubit from circuit file")
                        self.file.close()
                        self.file = None
                        return None

                    qc.addQubit(qubit, y)

        self.file.close()
        self.file = None
        return qc

    def readTutorialText(self, filename):
        if (filename == "" or filename == None):
            return None

        self.file = open("tutorial/text/" + filename + ".tut")
        text = self.file.read()
        self.file.close()
        self.file = None
        return text


    def readTutorialExercise(self, filename):
        if (filename == "" or filename == None):
            return None

        self.file = open("tutorial/exercises/" + filename + ".txr")
        text = self.file.read()
        lines = text.split("\n")
        text = ""
        ret = []
        firsttime = True
        for i in range(len(lines) - 1):
            if (lines[i][:3] != "%o%"):
                text += lines[i] + "\n"
            elif (firsttime):
                ret.append(text)
                ret.append(lines[i][3:])
                firsttime = False
            else:
                ret.append(lines[i][3:])

        self.file.close()
        self.file = None
        return ret

    def __init__(self):
        self.file = None


#fm = FileManager()
#qc = fm.readQuantumCircuit("circuit.cq")
#print("==============GOOD LUCK==============")
#print(qc.print())
