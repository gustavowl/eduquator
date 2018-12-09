from tkinter import *
from tkinter import ttk
from tutorialtopic import *

class ScreenTutorial(Frame):

    def createTopics(self, topicNames, topicTypes):
        #assert len(topicNames) == len(topicTypes)
        for i in range(len(topicNames)):

                self.labels.append(ttk.Label(self, text=topicNames[i]))
                self.labels[i].grid(column=0, row=i+1, sticky="nsew")

                self.tutorialTopics.append(TutorialTopic(topicNames[i], topicTypes[i]))

                if (i > 0):
                    #set this' previous info
                    self.tutorialTopics[i].setPrevious(self.tutorialTopics[i - 1])
                    #set previous' next info
                    self.tutorialTopics[i - 1].setNext(self.tutorialTopics[i])

    
    def __init__(self, parent=None, controller=None):

        Frame.__init__(self, parent)
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

        self.labels = []
        self.tutorialTopics = []

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        for i in range(len(topicNames) + 2):
            self.rowconfigure(i, weight=1)

        #creates Tutorial main label
        self.mainLabel = ttk.Label(self, text="TUTORIAL")
        self.mainLabel.grid(row=0, columnspan=2, sticky="nsew")

        #creates tutorial outline
        self.createTopics(topicNames, topicTypes)

        #creates "quit button"
        self.quit = ttk.Button(self, text="Quit")
        #TODO: add command
        self.quit.grid(row=len(topicNames)+1, columnspan=2, sticky="nsew")
