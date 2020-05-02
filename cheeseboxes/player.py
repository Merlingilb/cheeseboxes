

class player:
    def __init__(self, name, color, data):
        self.name = name
        self.color = color
        self.points = 0
        self.data = data

    def addPoint(self):
        self.points+=1

    def sendCommand(self, command, data=b""):
        self.data.outb += b"\x00" + command + data