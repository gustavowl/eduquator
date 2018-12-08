from tkinter import *
from tkinter import ttk
from layout.sidebar import *
from layout.simulator import *

class LayoutManager:
    def mainloop(self):
        self.root.mainloop()
        #self.screen.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.title("Eduquator")
        self.root.geometry("1080x720")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)


        self.screen = ttk.Frame(self.root, borderwidth=5, relief="sunken")
        self.screen.grid(row=0, column=0, sticky="nsew")
        self.screen.rowconfigure(0, weight=1)
        self.screen.columnconfigure(0, weight=1)
        self.screen.columnconfigure(1, weight=4)

        self.frames = {}
        for F in (Sidebar, Simulator):
            frame = F(parent=self.root, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Sidebar")

        """
        self.sideFrame = tk.Frame(self.screen, borderwidth=5, relief="sunken", bg="red")
        self.sideFrame.grid(row=0, column=0, sticky="nsew")
        self.sb = Sidebar(parent=self.sideFrame, controller=self)

        self.simulatorFrame = tk.Frame(self.screen, borderwidth=5, relief="sunken", bg="orange")
        self.simulatorFrame.grid(row=0, column=1, sticky="nsew")
        self.simulatorGrid = Simulator(parent=self.simulatorFrame, controller=self)"""

        #https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
        #self.screen2 = ttk.Frame...

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
