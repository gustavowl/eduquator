import numpy as np

class Qubit:

    def set0(self):
        self.setLabel("|0⟩")
        self.setVec(np.matrix("1; 0"))

    def set1(self):
        self.setLabel("|1⟩")
        self.setVec(np.matrix("0; 1"))

    def setPlus(self):
        self.setLabel("|+⟩")
        self.setVec(1/(2**0.5) * np.matrix("1; 1"))

    def setMinus(self):
        self.setLabel("|-⟩")
        self.setVec(1/(2**0.5) * np.matrix("1; -1"))

    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def setVec(self, vec):
        #assert vec \in np.matrix
        if (vec.size != 2):
            print("Error: Qubit is not a binary vector")
            return
        length = np.dot(vec.getH(), vec)
        error = 1e-10
        if (length > 1 + error or length < 1 - error):
            print("Error: Qubit is not unitary: " + str(length))
            print(vec)
            print("diff = " + str(length - 1))
            print()
            return
        
        self.vec = vec

    def getVec(self):
        return self.vec

    def print(self):
        print("Qubit label: " + self.label)
        print("Qubit vec:\n" + str(self.vec))

    def __init__(self):
        self.label = ""
        self.vec = np.matrix("0; 0")
