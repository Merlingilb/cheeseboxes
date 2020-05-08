import selectors
import socket
import time
import types

from game import game
from player import player

version = "1.0.1.1"

HOST = '0.0.0.0'
#HOST = '127.0.0.1'
PORT = 65432

sel = selectors.DefaultSelector()

games = list()

keyTest = None

globalData = []

def sendGameList():
    global sel, games
    gamelist = ""
    for game in games:
        if len(game[0].players) < 2:
            gamelist += "Game " + str(games.index(game)) + " with player: " + game[0].players[0].name + "," + str(hash(game[1][0].addr[0]+str(game[1][0].addr[1]))) + ";"
    for key in sel.get_map():
        try:
            client = sel.get_map()[key]
            client.data.outb += b"\x0D" + bytes(gamelist, "utf-8")
        except:
            pass

def addData(data, client):
    global globalData
    tempData = str(data, "utf-8").split("\x00")
    if not data[0:1] == b"\x00":
        j = -1
        for i, item in enumerate(globalData):
            if item[1] == client:
                j = i
        if j>=0:
            globalData[j][0] = globalData[j][0] + tempData[0]
        tempData.pop(0)
    for i in tempData:
        globalData.append([i, client])

def handle(data):
    global games
    if len(data[0]) > 0 and data[0][0] == "\x01" and data[0][1:] == version:
        data[1].outb += b"\x00\x02"
        games.append([game(player("1", "#00FF00", data[1])), [data[1]]])
    if len(data[0]) > 0 and data[0][0] == "\x05":
        for i in games:
            if data[1] in i[1]:
                args = data[0][1:].split(",")
                tempA = i[0].setWall((int(args[0]),int(args[1])), int(args[2]))
                tempB = i[0].setWall((int(args[3]),int(args[4])), int(args[5]))
                if tempA or tempB:
                    i[0].switchPlayer()
                i[0].waiting = False
    if len(data[0]) > 0 and data[0][0] == "\x06":
        for i in games:
            if data[1] in i[1]:
                if data[1] == i[0].players[0].data:
                    i[0].players[0].name = data[0][1:]
                    i[0].sendField(0)
                    i[0].players[0].ready = True
                if len(i[0].players)>1 and data[1] == i[0].players[1].data:
                    i[0].players[1].name = data[0][1:]
                    i[0].sendField(1)
                    i[0].players[1].ready = True
    if len(data[0]) > 0 and data[0][0] == "\x0B":
        for i in games:
            if data[1] in i[1]:
                i[0].quit()
                games.remove(i)
                break
    if len(data[0]) > 0 and data[0][0] == "\x0E" and data[0][1:].split(";")[0] == version:
        hashed = data[0][1:].split(";")[1]
        for i in games:
            thisHash = str(hash(i[1][0].addr[0]+str(i[1][0].addr[1])))
            if len(i[1]) < 2 and (not i[1][0] == data[1]) and hashed == thisHash:
                data[1].outb += b"\x00\x02"
                i[1].append(data[1])
                i[0].addPlayer(player("2", "#0000FF", data[1]))


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print("accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    global games
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        try:
            recv_data = sock.recv(2048)  # Should be ready to read
            if recv_data:
                addData(recv_data, data)
                print("Data received: ", recv_data)
            else:
                print("closing connection to", data.addr)
                sel.unregister(sock)
                sock.close()
                for i in games:
                    if data in i[1]:
                        i[0].quit()
                        games.remove(i)
                        break
        except:
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
            for i in games:
                if data in i[1]:
                    i[0].quit()
                    games.remove(i)
                    break
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing", repr(data.outb), "to", data.addr)
            try:
                sent = sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]
            except OSError:
                data.outb = b""
            print(data.outb)

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print("listening on", (HOST, PORT))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)
lastTimestamp = time.time()

try:
    while True:
        events = sel.select(timeout=None)
        a = sel
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
        if len(globalData)>0:
            handle(globalData.pop(0))
        if lastTimestamp < time.time() - 1:
            sendGameList()
            lastTimestamp = time.time()
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
