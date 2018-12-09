import tkinter as tk
from tutorialtopic import *
from layout.tutorialoutline import *

class ScreenTutorial(tk.Frame):

    def show_frame(self, frame):
        frame.tkraise()

    def summon(self, event):
        index = self.labels.index(event.widget)
        #frame = self.tutorialTopics[index]
        #frame.tkraise()
        #print("shouldve rosen")

    def createTopics(self, topicNames, topicTypes):
        #assert len(topicNames) == len(topicTypes)
        for i in range(len(topicNames)):

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
