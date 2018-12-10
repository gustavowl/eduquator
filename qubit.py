import numpy as np

class Qubit:

    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def setVec(self, vec):
        #assert vec \in np.array
        if (vec.size != 2):
            print("Error: Qubit is not a binary vector")
            return
        if (np.vdot(vec, vec) != 1 ):
            print("Error: Qubit is not unitary")
            return
        
        self.vec = vec

    def getVec(self):
        return self.vec


    def __init__(self):
        self.label = ""
        self.vec = np.array([0, 0])
