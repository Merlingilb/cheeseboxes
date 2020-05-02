from tkinter import Canvas


class field(Canvas):
    def __init__(self, master, game):
        Canvas.__init__(self, master, width=500, height=500)
        self.game = game
        self.bind("<Motion>", self.moved)
        self.bind("<Button-1>", self.click)
        self.updater()

    def click(self, event):
        lines = self.find_overlapping(event.x-5,event.y-5,event.x+5,event.y+5)
        if len(lines)>0:
            lineCoords = self.coords(lines[0])
            lineCoords = self.findFields(lineCoords[0],lineCoords[1],lineCoords[2],lineCoords[3])
            self.setWall(lineCoords)

    def setWall(self, lineCoords):
        a = self.game.setWall(lineCoords[0], lineCoords[1], lineCoords[2], lineCoords[3])
        #b = self.game.setWall(lineCoords[2], lineCoords[3])
        #if not (a or b):
            #self.game.switchPlayer()

    def moved(self, event):
        lines = self.find_overlapping(event.x-5,event.y-5,event.x+5,event.y+5)
        if len(lines)>0:
            lineCoords = self.coords(lines[0])
            lineCoords = self.findFields(lineCoords[0],lineCoords[1],lineCoords[2],lineCoords[3])
            self.setSelected(lineCoords)
        else:
            self.setSelected([(-1,-1),0])

    def setSelected(self, lineCoords):
        self.game.setSelected(lineCoords[0], lineCoords[1])

    def findFields(self, x1, y1, x2, y2):
        temp = x1
        x1 = y1
        y1 = temp
        temp = x2
        x2 = y2
        y2 = temp
        x1-=10
        y1-=10
        x2-=10
        y2-=10
        x1/=50
        y1/=50
        x2/=50
        y2/=50
        if x2>x1:
            return [(int(x1),int(y1)), 3, (int(x1),int(y1-1)), 1]
        else:
            return [(int(x1),int(y1)), 0, (int(x1-1),int(y1)), 2]

    def updater(self):
        self.delete("all")
        for box in self.game.boxes:
            if box.wallNorth:
                self.create_line(box.pos[1] * 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 50 + 10,
                                 box.pos[0] * 50 + 10, width=5)
            elif box.selectedNorth:
                self.create_line(box.pos[1] * 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 50 + 10,
                                 box.pos[0] * 50 + 10, fill="#FF0000", width=5)
            else:
                self.create_line(box.pos[1] * 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 50 + 10,
                                 box.pos[0] * 50 + 10, width=1)
            if box.wallEast:
                self.create_line(box.pos[1] * 50 + 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 50 + 10,
                                 box.pos[0] * 50 + 50 + 10, width=5)
            elif box.selectedEast:
                self.create_line(box.pos[1] * 50 + 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 50 + 10,
                                 box.pos[0] * 50 + 50 + 10, fill="#FF0000", width=5)
            else:
                self.create_line(box.pos[1] * 50 + 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 50 + 10,
                                 box.pos[0] * 50 + 50 + 10, width=1)
            if box.wallSouth:
                self.create_line(box.pos[1] * 50 + 10, box.pos[0] * 50 + 50 + 10, box.pos[1] * 50 + 50 + 10,
                                 box.pos[0] * 50 + 50 + 10, width=5)
            elif box.selectedSouth:
                self.create_line(box.pos[1] * 50 + 10, box.pos[0] * 50 + 50 + 10, box.pos[1] * 50 + 50 + 10,
                                 box.pos[0] * 50 + 50 + 10, fill="#FF0000", width=5)
            else:
                self.create_line(box.pos[1] * 50 + 10, box.pos[0] * 50 + 50 + 10, box.pos[1] * 50 + 50 + 10,
                                 box.pos[0] * 50 + 50 + 10, width=1)
            if box.wallWest:
                self.create_line(box.pos[1] * 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 10,
                                 box.pos[0] * 50 + 50 + 10, width=5)
            elif box.selectedWest:
                self.create_line(box.pos[1] * 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 10,
                                 box.pos[0] * 50 + 50 + 10, fill="#FF0000", width=5)
            else:
                self.create_line(box.pos[1] * 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 10,
                                 box.pos[0] * 50 + 50 + 10, width=1)
            if box.owner == 1:
                self.create_rectangle(box.pos[1] * 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 50 + 10,
                                      box.pos[0] * 50 + 50 + 10, fill="#0000FF")
            if box.owner == -1:
                self.create_rectangle(box.pos[1] * 50 + 10, box.pos[0] * 50 + 10, box.pos[1] * 50 + 50 + 10,
                                      box.pos[0] * 50 + 50 + 10, fill="#00FF00")
        self.after(100, self.updater)