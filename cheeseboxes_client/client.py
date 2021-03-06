import socket

from game import game
from box import box

version = "1.0.1.1"

HOST = '193.31.24.180'  # The server's hostname or IP address
#HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

gamePlay = None
data = None

globalData = []
queue = []

gamePlay = game(queue, version)

def send(data):
    s.sendall(data)

def addData(data):
    global globalData
    tempData = str(data, "utf-8").split("\x00")
    if not data[0:1] == b"\x00" and len(globalData)>0:
        globalData[-1] = globalData[-1] + tempData[0]
        tempData.pop(0)
    for i in tempData:
        globalData.append(i)

def handle(data):
    global gamePlay, queue
    if len(data) > 0 and data[0] == "\x03":
        boxes = list()
        boxData = data[1:].split(";")
        for boxDate in boxData[0:-1]:
            boxDate = boxDate.split(',')
            walls = list()
            if boxDate[2] == "True":
                walls.append(True)
            else:
                walls.append(False)
            if boxDate[3] == "True":
                walls.append(True)
            else:
                walls.append(False)
            if boxDate[4] == "True":
                walls.append(True)
            else:
                walls.append(False)
            if boxDate[5] == "True":
                walls.append(True)
            else:
                walls.append(False)
            owner = int(boxDate[6])
            boxes.append(box((int(boxDate[0]), int(boxDate[1])), walls, owner))
        gamePlay.boxes = boxes
    if len(data) > 0 and data[0] == "\x02":
        gamePlay.joined()
    if len(data) > 0 and data[0] == "\x04":
        gamePlay.enablePlay()
    if len(data) > 0 and data[0] == "\x07":
        gamePlay.winner()
    if len(data) > 0 and data[0] == "\x08":
        gamePlay.looser()
    if len(data) > 0 and data[0] == "\x09":
        pointsData = data[1:].split(";")
        text = ""
        text += pointsData[0] + "  " + pointsData[1] + " : " + pointsData[3] + "  " + pointsData[2]
        gamePlay.points(text)
    if len(data) > 0 and data[0] == "\x0A":
        gamePlay.newGame()
    if len(data) > 0 and data[0] == "\x0C":
        gamePlay.quitted()
    if len(data) > 0 and data[0] == "\x0D":
        gamePlay.gameList(data[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while 1:
        s.settimeout(0.1)
        try:
            data = s.recv(2048)
            print("Data: "+str(data,"utf-8"))
        except:
            data = b""
        if len(data)>0:
            addData(data)
        if len(globalData)>0:
            handle(globalData.pop(0))
        if len(queue)>0:
            if queue[0]=="SHUTDOWN":
                break
            send(queue.pop(0))

