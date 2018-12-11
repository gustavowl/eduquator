from tkinter import *
from tkinter import ttk
from layout.simulator import *
from threading import Thread, Lock, Condition
from time import sleep

class SimulatorControl(Frame):

    def play(self):
        x = 0
        while (self.alive):
            self.cv.acquire()

            while (self.isPaused):
                x = 0
                print("PAUSE " + str(x))
                self.cv.wait()

            sleep(0.1) #sleep a fraction of second before drawing
            x += 1
            self.underControl.drawPlayLine(x)

            self.cv.release()

    def pausePlay(self):
        if self.isPaused:
            self.cv.acquire()
            self.pausePlayButton["text"] = "||"
            self.isPaused = not self.isPaused
            self.cv.notify()
            self.cv.release()
            
        else:
            self.cv.acquire()
            self.pausePlayButton["text"] = "|⟩"
            self.isPaused = not self.isPaused
            self.cv.release()

    def createWidgets(self, onStopPressed):
        self.statusLabel = ttk.Label(self, text="Simulating")
        self.statusLabel.grid(column=1, row=0, columnspan=4)

        self.backButton = ttk.Button(self, text="<<")
        self.backButton.grid(column=1, row=1, sticky="nsew")

        self.isPaused = True
        self.pausePlayButton = ttk.Button(self, text="|⟩",
                command=self.pausePlay)
        self.pausePlayButton.grid(column=2, row=1, sticky="nsew")

        self.forwardButton = ttk.Button(self, text=">>")
        self.forwardButton.grid(column=3, row=1, sticky="nsew")

        self.stopButton = ttk.Button(self, text="[]",
                command=lambda: self.controller.show_frame(onStopPressed))
        self.stopButton.grid(column=4, row=1, sticky="nsew")

        for child in self.winfo_children():
            child.grid_configure(padx=3, pady=3)

    def __init__(self, parent, controller, onStopPressed, underControl):
        Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        self.underControl = underControl

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(5, weight=3)

        for row in range(4):
            self.rowconfigure(row+1, weight=1)

        self.createWidgets(onStopPressed)

        self.lk = Lock()
        self.cv = Condition(self.lk)
        self.threadPlay = Thread(target=self.play)
        self.alive = True
        self.threadPlay.start()

    def __del__(self):
        #TODO: call destructor
        print("IM NOT BEING CALLED")
        self.cv.acquire()
        self.alive = False
        self.isPaused = False
        self.cv.notify()
        self.cv.release()
        self.threadPlay.join()
        print("JOY")
