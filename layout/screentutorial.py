import tkinter as tk
from tutorialtopic import *
from layout.tutorialoutline import *
from layout.tutorialtext import *
from layout.tutorialtextandsimulator import *
from layout.tutorialexercise import *
from layout.tutorialexerciseandsimulator import *

class ScreenTutorial(tk.Frame):

    def show_frame(self, frame):
        if frame == self.parent:
            self.controller.show_frame("ScreenStart")
            return

        frame.tkraise()

    def createTopics(self, topicNames, topicTypes):
        #assert len(topicNames) == len(topicTypes)
        for i in range(len(topicNames)):

                if (topicTypes[i] == TopicType.TEXT):
                    self.tutorialTopics.append(TutorialText(self, self, topicNames[i]))
                elif (topicTypes[i] == TopicType.TEXT_AND_SIMULATOR):
                    self.tutorialTopics.append(TutorialTextAndSimulator(self, self,
                        topicNames[i]))
                elif (topicTypes[i] == TopicType.EXERCISE):
                    self.tutorialTopics.append(TutorialExercise(self, self,
                        topicNames[i]))
                elif (topicTypes[i] == TopicType.EXERCISE_AND_SIMULATOR):
                    self.tutorialTopics.append(TutorialExerciseAndSimulator(self, self,
                        topicNames[i]))
                else:
                    #self.tutorialTopics.append(TutorialTopic(self, self, topicNames[i],
                    #    topicTypes[i]))
                    print("ERROR AT SCREENTUTORIAL.CREATETOPICS\n")
                    return

                self.tutorialTopics[i].grid(row=0, column=0, sticky="nsew")

                if (i > 0):
                    #set this' previous info
                    self.tutorialTopics[i].setPrevious(self.tutorialTopics[i - 1])
                    #set previous' next info
                    self.tutorialTopics[i - 1].setNext(self.tutorialTopics[i])

    
    def __init__(self, parent=None, controller=None):

        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.grid(row = 0, column=0, sticky="nsew")

        topicNames = ["Introduction",
            "\tMotivation",
            "\tTopic1",
            "\tTopic2",
            "LinearAlgebra",
            "\tBasics",
            "\tInnerProduct",
            "\tUnitaryVector",
            "\tDiracNotation",
            "\tExercise1",
            "QuantumMechanics",
            "\tPostulates",
            "\tExercise2",
            "SimulatingCircuits",
            "\tHowTo",
            "\tHadamard",
            "\tExercise3",
            "QuantumAlgorithms",
            "\tQuantumTeleport",
            "\tShorAlgorithm",
            "\tExercise4"]
        topicTypes = [TopicType.TEXT,
            TopicType.TEXT, TopicType.TEXT, TopicType.TEXT,
            TopicType.TEXT, TopicType.TEXT, TopicType.TEXT, TopicType.TEXT, TopicType.TEXT,
            TopicType.EXERCISE,
            TopicType.TEXT, TopicType.TEXT, TopicType.EXERCISE,
            TopicType.TEXT, TopicType.TEXT_AND_SIMULATOR, TopicType.TEXT_AND_SIMULATOR,
            TopicType.EXERCISE_AND_SIMULATOR,
            TopicType.TEXT, TopicType.TEXT_AND_SIMULATOR, TopicType.TEXT_AND_SIMULATOR,
            TopicType.EXERCISE_AND_SIMULATOR]

        #creates tutorial outline
        self.tutorialTopics = []
        self.createTopics(topicNames, topicTypes)

        self.outline = TutorialOutline(self, self, self.tutorialTopics)
        self.outline.setCallerScreen(self.parent)
        for i in range(len(topicNames)):
            self.tutorialTopics[i].setOutline(self.outline)
