import numpy as np

class QuantumGate:

    def setIdentity(self):
        self.label = "Identity"
        self.setMatrix(np.matrix("1 0; 0 1"))

    def setHadamard(self):
        self.label = "Hadamard"
        self.setMatrix( 1/(2**0.5) * np.matrix("1 1; 1 -1") )

    def setCnot(self):
        self.label = "Controlled Not"
        self.setMatrix(np.matrix("1 0 0 0; 0 1 0 0; " +
            "0 0 0 1; 0 0 1 0"))

    def setXgate(self):
        self.label = "Pauli-X"
        self.setMatrix(np.matrix("0 1; 1 0"))

    def setYgate(self):
        self.label = "Pauli-Y"
        self.setMatrix(np.matrix("0 -1j; 1j 0"))

    def setZgate(self):
        self.label = "Pauli-Z"
        self.setMatrix(np.matrix("1 0; 0 -1"))

    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def setMatrix(self, matrix):
        #assert matrix \in np.matrix
        if (matrix[0].size != matrix.size / matrix[0].size):
            print("Error: not square matrix")
            return
        self.numberOfIOs = matrix[0].size / 2
        self.matrix = matrix

    def print(self):
        print("Gate label: " + self.label)
        print("Gate numberOfIOs: " + str(self.numberOfIOs))
        print("Gate matrix:\n" + str(self.matrix))

    def __init__(self):
        self.label = ""
        self.numberOfIOs = 0
        self.matrix = np.matrix([])
