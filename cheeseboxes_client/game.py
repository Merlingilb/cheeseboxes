import threading
from time import sleep

from box import box
from tkinter import *

from field import field
from animation import animation



class game(threading.Thread):
    def __init__(self, queue, version):
        self.version = version
        self.gameListData = list()
        self.master = None
        self.canvasAnimation = None
        self.canvas = None
        self.entryName = None
        self.buttonStart = None
        self.buttonJoin = None
        self.buttonNewGame = None
        self.buttonQuit = None
        self.labelNotifications = None
        self.labelInfos = None
        self.labelScore = None
        self.labelGameName = None
        self.frameCanvas1 = None
        self.frameInfos1 = None
        self.frameCanvas2 = None
        self.frameInfos2 = None
        self.frameStartName = None
        self.frameJoinGame = None
        self.frameJoinGameButtons = None
        self.gameLists = None
        threading.Thread.__init__(self)
        self.queue = queue
        self.enabled = False
        self.boxes = []
        self.start()

    def enablePlay(self):
        self.enabled = True
        self.labelNotifications.config(text="Play")

    def sendCommand(self, command, data=b""):
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
            self.labelNotifications.config(text="")
        return False

    def switchPlayer(self):
        self.i = (self.i + 1) % 2

    def setSelected(self, coords, direction):
        for box in self.boxes:
            if box.pos == coords:
                box.setSelected(direction)
            else:
                box.setSelected(-1)

    def joinGame(self):
        for i in self.gameListData:
            if self.gameLists.get(ACTIVE) in i:
                self.sendCommand(b"\x0E", bytes(self.version + ";" + i[1], "utf-8"))

    def joinNewGame(self):
        self.sendCommand(b"\x01", bytes(self.version, "utf-8"))

    def quitGame(self):
        self.sendCommand(b"\x0B")

    def quitted(self):
        self.frameCanvas2.grid_remove()
        self.frameInfos2.grid_remove()
        self.frameCanvas1.grid()
        self.frameInfos1.grid()
        self.boxes = []
        self.entryName.config(state='normal')
        self.buttonStart.config(state='normal')
        self.buttonStart.config(text="Start")
        self.labelNotifications.config(text="")
        self.labelScore.config(text="")
        self.labelInfos.config(text="The game has been quitted!")

    def joined(self):
        self.frameCanvas1.grid_remove()
        self.frameInfos1.grid_remove()
        self.frameCanvas2.grid()
        self.frameInfos2.grid()
        self.labelInfos.config(text="")

    def startGame(self):
        if len(self.entryName.get())<1:
            self.labelNotifications.config(text="Type your name!")
            return
        self.sendCommand(b"\x06", bytes(self.entryName.get(), "utf-8"))
        self.entryName.config(state='disabled')
        self.buttonStart.config(state='disabled')
        self.labelNotifications.config(text="")

    def newGame(self):
        self.entryName.config(state='normal')
        self.buttonStart.config(state='normal')
        self.buttonStart.config(text="Rematch")

    def winner(self):
        self.labelNotifications.config(text="Winner!")

    def looser(self):
        self.labelNotifications.config(text="Looser!")

    def points(self, text):
        self.labelScore.config(text=text)

    def gameList(self, data):
        if self.gameLists == None:
            return
        self.gameListData = list()
        for game in data.split(";"):
            if not game == "":
                self.gameListData.append(game.split(","))
        self.gameListData = [list(item) for item in set(tuple(row) for row in self.gameListData)]
        #toDelete = list()
        for i, listbox_entry in enumerate(self.gameLists.get(0, END)):
            if listbox_entry in [item[0] for item in self.gameListData]:
                continue
            else:
                self.gameLists.delete(i)
                #toDelete.append(listbox_entry)
        #for i in toDelete:
            #self.gameLists.delete(i)
        #self.gameLists.delete(0, END)
        toAdd = list()
        for game in self.gameListData:
            if game[0] in self.gameLists.get(0, END):
                continue
            else:
                toAdd.append(game[0])
        for i in toAdd:
            if len(self.gameLists.get(0, END)) > 0:
                for j, listbox_entry in enumerate(self.gameLists.get(0, END)):
                    if listbox_entry > i:
                        if j > 0:
                            self.gameLists.insert(j-1, i)
                        else:
                            self.gameLists.insert(0, i)
                    else:
                        a = len(self.gameLists.get(0, END))
                        b = self.gameLists.get(0, END)
                        if len(self.gameLists.get(0, END)) <= j+1:
                            self.gameLists.insert(END, i)
            else:
                self.gameLists.insert(0, i)

    def shutdown(self):
        self.queue.append("SHUTDOWN")
        self.master.destroy()

    def run(self):
        self.master = Tk()
        self.master.protocol("WM_DELETE_WINDOW", self.shutdown)
        self.frameCanvas1 = Frame(self.master)
        self.frameCanvas1.grid(row=0,column=0)
        self.frameInfos1 = Frame(self.master)
        self.frameInfos1.grid(row=1,column=0)
        self.frameCanvas2 = Frame(self.master)
        self.frameCanvas2.grid(row=0,column=0)
        self.frameInfos2 = Frame(self.master)
        self.frameInfos2.grid(row=1,column=0)
        self.frameCanvas2.grid_remove()
        self.frameInfos2.grid_remove()

        self.labelGameName = Label(self.frameCanvas1, text="Cheese Boxes", font="Verdana 30 bold", fg="blue")
        self.labelGameName.grid(row=0,column=0)
        self.canvasAnimation = animation(self.frameCanvas1)
        self.canvasAnimation.grid(row=1,column=0)
        self.frameJoinGame = Frame(self.frameInfos1)
        self.frameJoinGame.grid(row=0,column=0)
        self.gameLists = Listbox(master=self.frameJoinGame, selectmode='browse', width=50)
        self.gameLists.grid(row=0,column=0)
        self.frameJoinGameButtons = Frame(self.frameJoinGame)
        self.frameJoinGameButtons.grid(row=0,column=1)
        self.buttonJoin = Button(self.frameJoinGameButtons, text="Join a game", command=self.joinGame)
        self.buttonJoin.grid(row=0,column=0)
        self.buttonNewGame = Button(self.frameJoinGameButtons, text="New game", command=self.joinNewGame)
        self.buttonNewGame.grid(row=1,column=0)
        self.labelInfos = Label(self.frameInfos1, text="", font="Verdana 20 bold")
        self.labelInfos.grid(row=1,column=0)

        self.canvas = field(self.frameCanvas2, self)
        self.canvas.grid(row=0,column=0)
        self.frameStartName = Frame(self.frameInfos2)
        self.frameStartName.grid(row=0,column=0)
        self.entryName = Entry(self.frameStartName)
        self.entryName.grid(row=0,column=0)
        self.buttonStart = Button(self.frameStartName, text="Start", command=self.startGame)
        self.buttonStart.grid(row=0,column=1)
        self.buttonQuit = Button(self.frameStartName, text="Quit", command=self.quitGame)
        self.buttonQuit.grid(row=0,column=2)
        self.labelNotifications = Label(self.frameInfos2, text="", font="Verdana 30 bold", fg="red")
        self.labelNotifications.grid(row=1,column=0)
        self.labelScore = Label(self.frameInfos2, text="", font="Verdana 20 bold")
        self.labelScore.grid(row=2,column=0)
        self.master.mainloop()
