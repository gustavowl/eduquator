import quantumgate
import qubit

class QuantumCircuit:

    def addQubit(self, qubit, posy):
        #posx == 0
        if (posy >= 0 and posy < len(self.circuit)):
            self.circuit[posy] = qubit
            return
        if (posy >= 0 and posy == len(self.circuit)):
            row = [qubit]
            if (len(self.circuit) == 0):
                self.circuit.append(row)
            else:
                identity = QuantumGate()
                identity.setIdentity()
                for i in range(len(self.circuit[0]) - 1):
                    row.append(None)
                    self.addGate(identity, i + 1, posy)
                self.circuit.append(row)

            return
        print("Error: row jump")


    def addGate(self, gate, posx, posy):
        #assert gate \in QuantumGate
        if (posx > 0):
            if (len(self.circuit) < posy and len(self.circuit[posy]) < posx):
                self.circuit[posy][posx] = gate
            else:
                print("Error. Invalid dimensions")
        else:
            print("Error. Expected qubit in posx 1, not quantum gate")

    def __init__(self):
        self.circuit = []
