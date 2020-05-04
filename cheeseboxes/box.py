class box:
    def __init__(self, pos, walls):
        self.pos = pos
        self.wallNorth = walls[0]
        self.wallEast = walls[1]
        self.wallSouth = walls[2]
        self.wallWest = walls[3]
        self.owner = None
        self.selectedNorth = False
        self.selectedEast = False
        self.selectedSouth = False
        self.selectedWest = False

    def setWall(self, direction):
        if direction == 0:
            self.wallNorth = True
            self.selectedNorth = False
        elif direction == 1:
            self.wallEast = True
            self.selectedEast = False
        elif direction == 2:
            self.wallSouth = True
            self.selectedSouth = False
        elif direction == 3:
            self.wallWest = True
            self.selectedWest = False
        if self.wallNorth and self.wallEast and self.wallSouth and self.wallWest:
            return 1
        return 0

    def setOwner(self, player):
        self.owner = player
        #player.addPoint()

    def getWalls(self):
        return [self.wallNorth, self.wallEast, self.wallSouth, self.wallWest]

    def getWallNumber(self):
        i = 0
        if self.wallNorth:
            i += 1
        if self.wallEast:
            i += 1
        if self.wallSouth:
            i += 1
        if self.wallWest:
            i += 1
        return i

    def setSelected(self, direction):
        if direction == 0 and not self.wallNorth:
            self.selectedNorth = True
        if direction == 1 and not self.wallEast:
            self.selectedEast = True
        if direction == 2 and not self.wallSouth:
            self.selectedSouth = True
        if direction == 3 and not self.wallWest:
            self.selectedWest = True
        if direction == -1:
            self.selectedNorth = False
            self.selectedEast = False
            self.selectedSouth = False
            self.selectedWest = False
