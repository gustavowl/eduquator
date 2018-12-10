import numpy as np

class QuantumGate:

    def setIdentity():
        self.label = "Identity"
        self.setMatrix(np.matrix("1 0; 0 1"))

    def setHadamard():
        self.label = "Hadamard"
        self.setMatrix( 1/(2**0.5) * np.matrix("1 1; 1 -1") )

    def setCnot():
        self.label = "Controlled Not"
        self.setMatrix(np.matrix("1 0 0 0; 0 1 0 0; " +
            "0 0 0 1; 0 0 1 0"))

    def setXgate():
        self.label = "Pauli-X"
        self.setMatrix(np.matrix("0 1; 1 0"))

    def setYgate():
        self.label = "Pauli-Y"
        self.setMatrix(np.matrix("0 -1j; 1j 0"))

    def setZgate():
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
        self.numberOfIOs = matrix[0].size
        self.matrix = matrix

    def __init__(self):
        self.label = ""
        self.numberOfIOs = 0
        self.matrix = np.matrix([])
