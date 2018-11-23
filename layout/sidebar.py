from tkinter import *
from tkinter import ttk

class Sidebar(Frame):
    #widgets

    def createWidgets(self):
        print "qwertyuio"
        self.var = 73


content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="sunken",
        width=320, height=640)
tools_label = ttk.Label(frame, text="Tools")
button1 = ttk.Button(frame, text="1")
button2 = ttk.Button(frame, text="2")
button3 = ttk.Button(frame, text="3")
button4 = ttk.Button(frame, text="4")
tools_separator = ttk.Separator(frame, orient=HORIZONTAL)
circuit_label = ttk.Label(frame, text="Circuit Components")

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=2, rowspan=5)
#widgets
tools_label.grid(column=0, row=0, columnspan=2)
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=0, row=2)
button4.grid(column=1, row=2)
tools_separator.grid(row=3, columnspan=2, sticky=(W, E))
circuit_label.grid(row=4, columnspan=2)

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        #self.pack()
        self.createWidgets()

root = Tk()
sb = Sidebar(parent=root)
#print sb.var #works
sb.mainloop()

"""
content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="sunken",
        width=320, height=640)
tools_label = ttk.Label(frame, text="Tools")
button1 = ttk.Button(frame, text="1")
button2 = ttk.Button(frame, text="2")
button3 = ttk.Button(frame, text="3")
button4 = ttk.Button(frame, text="4")
tools_separator = ttk.Separator(frame, orient=HORIZONTAL)
circuit_label = ttk.Label(frame, text="Circuit Components")

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=2, rowspan=5)
#widgets
tools_label.grid(column=0, row=0, columnspan=2)
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=0, row=2)
button4.grid(column=1, row=2)
tools_separator.grid(row=3, columnspan=2, sticky=(W, E))
circuit_label.grid(row=4, columnspan=2)

for child in frame.winfo_children():
    child.grid_configure(padx=3, pady=3)


root.mainloop()"""
