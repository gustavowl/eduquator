from tkinter import *
from tkinter import ttk

class Sidebar(Frame):
    #widgets

    def createWidgets(self):
        self.fr = ttk.Frame(self, borderwidth=5, relief="sunken",
                width=320, height=640)
        self.tools_label = ttk.Label(self.fr, text="Tools")
        self.button1 = ttk.Button(self.fr, text="1")
        self.button2 = ttk.Button(self.fr, text="2")
        self.button3 = ttk.Button(self.fr, text="3")
        self.button4 = ttk.Button(self.fr, text="4")
        self.tools_separator = ttk.Separator(self.fr, orient=HORIZONTAL)
        self.circuit_label = ttk.Label(self.fr, text="Circuit Components")

        self.fr.grid(column=0, row=0)
        self.tools_label.grid(column=0, row=0, columnspan=2)
        self.button1.grid(column=0, row=1)
        self.button2.grid(column=1, row=1)
        self.button3.grid(column=0, row=2)
        self.button4.grid(column=1, row=2)
        self.tools_separator.grid(row=3, columnspan=2, sticky=(W, E))
        self.circuit_label.grid(row=4, columnspan=2)

        for child in self.fr.winfo_children():
            child.grid_configure(padx=3, pady=3)

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.createWidgets()

root = Tk()
sb = Sidebar(parent=root)
#print sb.var #works
sb.mainloop()

