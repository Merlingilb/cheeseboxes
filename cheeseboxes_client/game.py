import threading
from time import sleep

from box import box
from tkinter import *

from field import field



class game(threading.Thread):
    def __init__(self, queue):
        self.master = None
        self.canvas = None
        self.entry = None
        self.button = None
        self.label = None
        threading.Thread.__init__(self)
        self.queue = queue
        self.enabled = False
        self.test = 50
        self.boxes = []
        self.start()
        self.i = 0

    def enablePlay(self):
        self.enabled = True
        self.label.config(text="Play")

    def sendCommand(self, command, data):
        self.queue.append(b"\x00" + command + data)

    def getTest(self):
        return self.test

    def setWall(self, coords1, direction1, coords2, direction2):
        if self.enabled:
            for box in self.boxes:
                if box.pos == coords1:
                    if box.wallNorth and direction1==0:
                        return False
                    if box.wallEast and direction1==1:
                        return False
                    if box.wallSouth and direction1==2:
                        return False
                    if box.wallWest and direction1==3:
                        return False
                    box.setWall(direction1)
                if box.pos == coords2:
                    if box.wallNorth and direction2==0:
                        return False
                    if box.wallEast and direction2==1:
                        return False
                    if box.wallSouth and direction2==2:
                        return False
                    if box.wallWest and direction2==3:
                        return False
                    box.setWall(direction2)
            args = ""
            args += str(coords1[0]) + "," + str(coords1[1])
            args += "," + str(direction1) + ","
            args += str(coords2[0]) + "," + str(coords2[1])
            args += "," + str(direction2)
            self.sendCommand(b"\x05", bytes(args, "utf-8"))
            self.enabled = False
            self.label.config(text="")
        return False

    def switchPlayer(self):
        self.i = (self.i + 1) % 2

    def setSelected(self, coords, direction):
        for box in self.boxes:
            if box.pos == coords:
                box.setSelected(direction)
            else:
                box.setSelected(-1)

    def startGame(self):
        self.sendCommand(b"\x06", bytes(self.entry.get(), "utf-8"))
        self.entry.config(state='disabled')
        self.label.config(text="")

    def winner(self):
        self.label.config(text="Winner!")

    def looser(self):
        self.label.config(text="Looser!")

    def run(self):
        self.master = Tk()
        self.canvas = field(self.master, self)
        self.canvas.pack()
        self.entry = Entry(self.master)
        self.entry.pack()
        self.button = Button(self.master, text="Start", command=self.startGame)
        self.button.pack()
        self.label = Label(self.master, text="", font="Verdana 30 bold", fg="red")
        self.label.pack()
        self.master.mainloop()
