from enum import Enum
import tkinter as tk

class TopicType(Enum):
    TEXT = 1
    TEXT_AND_SIMULATOR = 2
    EXERCISE = 3
    EXERCISE_AND_SIMULATOR = 4

class TutorialTopic(tk.Frame):
    def setPrevious(self, previous):
        #assert previous \in TutorialTopic
        self.previous = previous
        self.buttonPrevious = tk.Button(self, text="<--",
                command=lambda: self.controller.show_frame(self.previous))

    def getPrevious(self):
        return self.previous

    def setNext(self, next):
        #assert next \in TutorialTopic
        self.next = next
        self.next = next
        self.buttonNext = tk.Button(self, text="-->",
                command=lambda: self.controller.show_frame(self.next))
    
    def setOutline(self, outline):
        #assert outline \in Frame
        self.outline = outline

    def getNext(self):
        return self.next

    #tutorial/actual.should be name.
    #tutorial/actual.tut correspond to file containg tutorial text
    #tutorial/actual.txr corresponds to file containg exercise
    #tutorial/actual.qc contains quantum circuit for simulation
    def getActual(self):
        return self.actual
        
    def __init__(self, parent, controller, actual, topictype):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.previous = None
        self.actual = actual
        self.next = None

        self.buttonPrevious = None
        self.buttonNext = None

        self.outline = None
        self.topictype = topictype
