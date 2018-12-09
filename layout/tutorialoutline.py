import tkinter as tk
from tutorialtopic import *

class TutorialOutline(tk.Frame):

    def summon(self, event):
        print(event.widget)
        index = self.labels.index(event.widget)
        print(index)
        
    def bindToFrames(self, tutorialFrames):
        print("TODO")

    def __init__(self, parent=None, controller=None, tutorialTopics=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row = 0, column = 0, sticky="nsew")

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.labels = []

        #creates Tutorial main label
        self.mainLabel = tk.Label(self, text="TUTORIAL")
        self.mainLabel.grid(row=0, columnspan=2, sticky="nsew")

        #creates tutorial outline
        for i in range(len(tutorialTopics)):
            self.labels.append(tk.Label(self, text=tutorialTopics[i].getActual(),
                fg="blue"))
            self.labels[i].grid(column=0, row=i+1, sticky="nsew")
            self.labels[i].bind("<Button-1>", self.summon)

        #creates "quit button"
        self.quit = tk.Button(self, text="Quit", command=lambda:
                self.controller.show_frame("ScreenStart"))
        self.quit.grid(row=len(tutorialTopics)+1, columnspan=2, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        for i in range(len(tutorialTopics) + 2):
            self.rowconfigure(i, weight=1)
