from tkinter import *
from tkinter import ttk
from layout.screenstart import *
from layout.screensimulator import *
from layout.screentutorial import *

class LayoutManager:
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
            frame = F(parent=self.root, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("ScreenStart")

        #https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
        #self.startScreen2 = ttk.Frame...

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
