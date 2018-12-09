import tkinter as tk
from tutorialtopic import *
from layout.tutorialoutline import *
from layout.tutorialtext import *

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
                else:
                    self.tutorialTopics.append(TutorialTopic(self, self, topicNames[i],
                        topicTypes[i]))

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

        topicNames = ["Type 1",
            "Type 2",
            "\tIdented",
            "Type 3",
            "Type 4"]
        topicTypes = [TopicType.TEXT,
            TopicType.TEXT_AND_SIMULATOR,
            TopicType.TEXT,
            TopicType.EXERCISE,
            TopicType.EXERCISE_AND_SIMULATOR]

        #creates tutorial outline
        self.tutorialTopics = []
        self.createTopics(topicNames, topicTypes)

        self.outline = TutorialOutline(self, self, self.tutorialTopics)
        self.outline.setCallerScreen(self.parent)
        for i in range(len(topicNames)):
            self.tutorialTopics[i].setOutline(self.outline)
