from enum import Enum

class TopicType(Enum):
    TEXT = 1
    TEXT_AND_SIMULATOR = 2
    EXERCISE = 3
    EXERCISE_AND_SIMULATOR = 4

class TutorialTopic:
    def setPrevious(self, previous):
        #assert previous \in TutorialTopic
        self.previous = previous

    def getPrevius(self):
        return self.previous

    def setNext(self, next):
        #assert next \in TutorialTopic
        self.next = next

    def getNext(self):
        return self.next

    #tutorial/actual.should be name.
    #tutorial/actual.tut correspond to file containg tutorial text
    #tutorial/actual.txr corresponds to file containg exercise
    #tutorial/actual.qc contains quantum circuit for simulation
    def getActual(self):
        return self.actual
        
    def __init__(self, actual, topictype):
        self.previous = None
        self.actual = actual
        self.next = None
        self.topictype = topictype
