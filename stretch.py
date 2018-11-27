from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Lilo & Stretch")
root.geometry("320x640")
frame = ttk.Frame(root, borderwidth=5, relief="sunken", width=320, height=640)
button = ttk.Button(frame, text="test")

frame.grid(sticky="nsew", row=0, column=0)
button.grid(sticky="nsew", row=0, column=0)
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame.mainloop()
