from tkinter import *
from tkinter import ttk
from layout.sidebar import *

class LayoutManager:
    def mainloop(self):
        self.sb.mainloop()

    def __init__(self):
        self.root = Tk()
        self.sb = Sidebar(parent=self.root)
