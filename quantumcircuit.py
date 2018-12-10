from quantumgate import *
from qubit import *

class QuantumCircuit:

    def getCircuit(self):
        return self.circuit

    def addQubit(self, qubit, posy):
        #posx == 0
        if (posy >= 0 and posy < len(self.circuit)):
            self.circuit[posy][0] = qubit
            return
        if (posy >= 0 and posy == len(self.circuit)):
            row = [qubit]
            self.circuit.append(row)
            if (len(self.circuit) > 0):
                identity = QuantumGate()
                identity.setIdentity()
                for i in range(len(self.circuit[0]) - 1):
                    #row.append(None)
                    self.addGate(identity, i + 1, posy)

            return
        print("Error: row jump")

    def guaranteeCircuitDimensions(self, dim):

        for y in range(len(self.circuit)):
            row = self.circuit[y]
            if (len(row) < dim):
                diff = dim - len(row)
                for i in range(diff):
                    identity = QuantumGate()
                    identity.setIdentity()
                    self.circuit[y].append(identity)

    def addGate(self, gate, posx, posy):
        #assert gate \in QuantumGate
        if (posx > 0):
            if (posy >= 0 and posy < len(self.circuit)):
                if (posx < len(self.circuit[posy])):
                    self.circuit[posy][posx] = gate
                elif (posx == len(self.circuit[posy])):
                    self.circuit[posy].append(gate)
                    #self.guaranteeCircuitDimensions(posx + 1)
                else:
                    print("Error. Invalid dimensions")
            else:
                print("Error. Invalid dimensions. posx = " + str(posx) +
                        " posy = " + str(posy))
                print("self.circuit length:" + str(len(self.circuit)))
                print("self.circuit[posy] length:" + str(len(self.circuit[posy])))
                print()
        else:
            print("Error. Expected qubit in posx 1, not quantum gate")

    def print(self):
        for y in range(len(self.circuit)):
            for x in range(len(self.circuit[y])):
                self.circuit[y][x].print()
                print()
            print("=======LINE FINISHED==========")

    def __init__(self):
        self.circuit = []
