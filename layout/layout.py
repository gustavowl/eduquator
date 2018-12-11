from tkinter import *
from tkinter import ttk
import tkinter as tk
from layout.screenstart import *
from layout.screensimulator import *
from layout.screentutorial import *
from filemanager import *
from layout.tutorialtext import *

class LayoutManager:
    def clicked(self, label):
        fm = FileManager()
        print(label)
        print("OPEN NEW WINDOW")
        window = Toplevel(self.root)
        tt = TutorialText(window, window, label)


    def mainloop(self):
        self.root.mainloop()
        #self.startScreen.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.title("Eduquator")
        self.root.geometry("1080x720")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.frames = {}

        for F in (ScreenStart, ScreenSimulator, ScreenTutorial):
            if (F != ScreenSimulator):
                frame = F(parent=self.root, controller=self)
            else:
                frame = F(parent=self.root, controller=self, 
                        onStopPressed = "ScreenStart")
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("ScreenStart")

        #https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
        #self.startScreen2 = ttk.Frame...

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if (page_name == "ScreenSimulator"):
            self.frames[page_name].setCircuit( self.frames["ScreenStart"].getCircuit() )
        frame.tkraise()
