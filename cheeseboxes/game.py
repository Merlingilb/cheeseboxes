import threading
import time
from random import randint
from time import sleep

import generator
from box import box
from tkinter import *

from field import field
from player import player


class game(threading.Thread):
    def __init__(self, player):
        threading.Thread.__init__(self)
        self.test = 50
        self.boxes = self.generateField()
        self.players = [player]
        self.i = 0
        self.waiting = False
        self.ready=-2
        self.start()

    def addPlayer(self, player):
        self.players.append(player)

    def sendField(self, i=-1):
        for j, player in enumerate(self.players):
            if i>=0 and not i==j:
                continue
            boxes = b""
            for box in self.boxes:
                if box.owner == player:
                    owner = 1
                elif box.owner == None:
                    owner = 0
                else:
                    owner = -1
                boxes += bytes(str(box.pos[0]), "utf-8")
                boxes += b","
                boxes += bytes(str(box.pos[1]), "utf-8")
                boxes += b","
                boxes += bytes(str(box.wallNorth), "utf-8")
                boxes += b","
                boxes += bytes(str(box.wallEast), "utf-8")
                boxes += b","
                boxes += bytes(str(box.wallSouth), "utf-8")
                boxes += b","
                boxes += bytes(str(box.wallWest), "utf-8")
                boxes += b","
                boxes += bytes(str(owner), "utf-8")
                boxes += b";"
            player.sendCommand(b"\x03", boxes)

    def getTest(self):
        return self.test

    def setWall(self, coords, direction):
        for box in self.boxes:
            if box.pos == coords:
                if box.setWall(direction):
                    box.setOwner(self.players[self.i])
                    return True
        return False

    def switchPlayer(self):
        self.i = (self.i + 1) % 2

    def setSelected(self, coords, direction):
        for box in self.boxes:
            if box.pos == coords:
                box.setSelected(direction)
            else:
                box.setSelected(-1)

    def endGame(self):
        for box in self.boxes:
            if box.owner == None:
                return False
        return True

    def countPoints(self, player):
        points = 0
        for box in self.boxes:
            if box.owner == player:
                points += 1
        return points

    def winner(self):
        p0 = self.countPoints(self.players[0])
        p1 = self.countPoints(self.players[1])
        if p0 > p1:
            return [self.players[0]]
        elif p1 > p0:
            return [self.players[1]]
        return [self.players[0], self.players[1]]

    def looser(self):
        p0 = self.countPoints(self.players[0])
        p1 = self.countPoints(self.players[1])
        if p0 > p1:
            return [self.players[1]]
        elif p1 > p0:
            return [self.players[0]]
        return []

    def run(self):
        while 1:
            while self.ready<0:
                time.sleep(0.1)
            self.i = randint(0,1)
            text0 = self.players[0].name + ";" + str(self.players[0].points) + ";" + self.players[1].name + ";" + str(self.players[1].points)
            self.players[0].sendCommand(b"\x09" + bytes(text0, "utf-8"))
            text1 = self.players[1].name + ";" + str(self.players[1].points) + ";" + self.players[0].name + ";" + str(self.players[0].points)
            self.players[1].sendCommand(b"\x09" + bytes(text1, "utf-8"))
            while 1:
                self.sendField()
                self.waiting = True
                self.nextPlayer()
                while self.waiting:
                    time.sleep(0.02)
                self.switchPlayer()
                if self.endGame():
                    break
            self.sendField()
            winner = self.winner()
            for player in winner:
                player.sendCommand(b"\x07")
                player.addPoint()
            looser = self.looser()
            for player in looser:
                player.sendCommand(b"\x08")
            text0 = self.players[0].name + ";" + str(self.players[0].points) + ";" + self.players[1].name + ";" + str(self.players[1].points)
            self.players[0].sendCommand(b"\x09" + bytes(text0, "utf-8"))
            text1 = self.players[1].name + ";" + str(self.players[1].points) + ";" + self.players[0].name + ";" + str(self.players[0].points)
            self.players[1].sendCommand(b"\x09" + bytes(text1, "utf-8"))
            self.boxes = self.generateField()
            self.ready=-2

    def nextPlayer(self):
        self.players[self.i].sendCommand(b"\x04")

    def generateField(self):
        field = generator.generate()
        return field
