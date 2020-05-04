from random import randint

from box import box

def generate():
    fields = list()
    field = list()
    field.append(box((0, 0), [True, False, False, True]))
    field.append(box((0, 1), [True, False, False, False]))
    field.append(box((0, 2), [True, False, False, False]))
    field.append(box((0, 3), [True, False, False, False]))
    field.append(box((0, 4), [True, False, False, False]))
    field.append(box((0, 5), [True, True, False, False]))
    field.append(box((1, 0), [False, False, False, True]))
    field.append(box((1, 1), [False, False, False, False]))
    field.append(box((1, 2), [False, False, False, False]))
    field.append(box((1, 3), [False, False, False, False]))
    field.append(box((1, 4), [False, False, False, False]))
    field.append(box((1, 5), [False, True, True, False]))
    field.append(box((2, 0), [False, False, False, True]))
    field.append(box((2, 1), [False, False, False, False]))
    field.append(box((2, 2), [False, False, False, False]))
    field.append(box((2, 3), [False, False, False, False]))
    field.append(box((2, 4), [False, True, False, False]))
    field.append(box((3, 0), [False, False, True, True]))
    field.append(box((3, 1), [False, False, True, False]))
    field.append(box((3, 2), [False, False, False, False]))
    field.append(box((3, 3), [False, False, False, False]))
    field.append(box((3, 4), [False, True, False, False]))
    field.append(box((4, 2), [False, False, False, True]))
    field.append(box((4, 3), [False, False, False, False]))
    field.append(box((4, 4), [False, False, False, False]))
    field.append(box((4, 5), [True, True, False, False]))
    field.append(box((5, 2), [False, False, True, True]))
    field.append(box((5, 3), [False, False, True, False]))
    field.append(box((5, 4), [False, False, True, False]))
    field.append(box((5, 5), [False, True, True, False]))
    fields.append(field)
    field = list()
    field.append(box((0, 1), [True, False, False, True]))
    field.append(box((0, 2), [True, False, False, False]))
    field.append(box((0, 3), [True, True, False, False]))
    field.append(box((1, 1), [False, False, False, True]))
    field.append(box((1, 2), [False, False, False, False]))
    field.append(box((1, 3), [False, False, False, False]))
    field.append(box((1, 4), [True, False, False, False]))
    field.append(box((1, 5), [True, True, False, False]))
    field.append(box((2, 0), [True, False, False, True]))
    field.append(box((2, 1), [False, False, False, False]))
    field.append(box((2, 2), [False, False, False, False]))
    field.append(box((2, 3), [False, False, False, False]))
    field.append(box((2, 4), [False, False, False, False]))
    field.append(box((2, 5), [False, True, True, False]))
    field.append(box((3, 0), [False, False, False, True]))
    field.append(box((3, 1), [False, False, False, False]))
    field.append(box((3, 2), [False, False, False, False]))
    field.append(box((3, 3), [False, False, False, False]))
    field.append(box((3, 4), [False, True, True, False]))
    field.append(box((4, 0), [False, False, True, True]))
    field.append(box((4, 1), [False, False, True, False]))
    field.append(box((4, 2), [False, False, False, False]))
    field.append(box((4, 3), [False, True, False, False]))
    field.append(box((5, 2), [False, False, False, True]))
    field.append(box((5, 3), [False, False, False, False]))
    field.append(box((5, 4), [True, False, False, False]))
    field.append(box((5, 5), [True, True, False, False]))
    field.append(box((6, 2), [False, False, True, True]))
    field.append(box((6, 3), [False, False, True, False]))
    field.append(box((6, 4), [False, False, True, False]))
    field.append(box((6, 5), [False, True, True, False]))
    fields.append(field)
    field = list()
    field.append(box((0, 2), [True, False, False, True]))
    field.append(box((0, 3), [True, True, False, False]))
    field.append(box((1, 2), [False, False, False, True]))
    field.append(box((1, 3), [False, False, False, False]))
    field.append(box((1, 4), [True, True, False, False]))
    field.append(box((2, 0), [True, False, False, True]))
    field.append(box((2, 1), [True, False, False, False]))
    field.append(box((2, 2), [False, False, False, False]))
    field.append(box((2, 3), [False, False, False, False]))
    field.append(box((2, 4), [False, False, False, False]))
    field.append(box((2, 5), [True, True, False, False]))
    field.append(box((3, 0), [False, False, False, True]))
    field.append(box((3, 1), [False, False, False, False]))
    field.append(box((3, 2), [False, False, False, False]))
    field.append(box((3, 3), [False, False, True, False]))
    field.append(box((3, 4), [False, False, True, False]))
    field.append(box((3, 5), [False, True, False, False]))
    field.append(box((4, 0), [False, False, False, True]))
    field.append(box((4, 1), [False, False, False, False]))
    field.append(box((4, 2), [False, True, False, False]))
    field.append(box((4, 5), [False, True, False, True]))
    field.append(box((5, 0), [False, False, True, True]))
    field.append(box((5, 1), [False, False, False, False]))
    field.append(box((5, 2), [False, True, False, False]))
    field.append(box((5, 4), [True, False, False, True]))
    field.append(box((5, 5), [False, True, False, False]))
    field.append(box((6, 1), [False, False, True, True]))
    field.append(box((6, 2), [False, True, True, False]))
    field.append(box((6, 4), [False, False, True, True]))
    field.append(box((6, 5), [False, True, True, False]))
    fields.append(field)
    field = list()
    field.append(box((0, 0), [True, False, False, True]))
    field.append(box((0, 1), [True, False, False, False]))
    field.append(box((0, 2), [True, True, False, False]))
    field.append(box((0, 6), [True, False, False, True]))
    field.append(box((0, 7), [True, False, False, False]))
    field.append(box((0, 8), [True, True, False, False]))
    field.append(box((1, 0), [False, False, False, True]))
    field.append(box((1, 1), [False, False, False, False]))
    field.append(box((1, 2), [False, False, False, False]))
    field.append(box((1, 3), [True, False, False, False]))
    field.append(box((1, 4), [True, False, True, False]))
    field.append(box((1, 5), [True, False, False, False]))
    field.append(box((1, 6), [False, False, False, False]))
    field.append(box((1, 7), [False, False, False, False]))
    field.append(box((1, 8), [False, True, False, False]))
    field.append(box((2, 0), [False, False, True, True]))
    field.append(box((2, 1), [False, False, False, False]))
    field.append(box((2, 2), [False, False, False, False]))
    field.append(box((2, 3), [False, True, True, False]))
    field.append(box((2, 5), [False, False, True, True]))
    field.append(box((2, 6), [False, False, False, False]))
    field.append(box((2, 7), [False, False, False, False]))
    field.append(box((2, 8), [False, True, True, False]))
    field.append(box((3, 1), [False, False, False, True]))
    field.append(box((3, 2), [False, True, True, False]))
    field.append(box((3, 6), [False, False, True, True]))
    field.append(box((3, 7), [False, True, False, False]))
    field.append(box((4, 1), [False, True, False, True]))
    field.append(box((4, 7), [False, True, False, True]))
    field.append(box((5, 1), [False, False, False, True]))
    field.append(box((5, 2), [True, True, False, False]))
    field.append(box((5, 6), [True, False, False, True]))
    field.append(box((5, 7), [False, True, False, False]))
    field.append(box((6, 0), [True, False, False, True]))
    field.append(box((6, 1), [False, False, False, False]))
    field.append(box((6, 2), [False, False, False, False]))
    field.append(box((6, 3), [True, True, False, False]))
    field.append(box((6, 5), [True, False, False, True]))
    field.append(box((6, 6), [False, False, False, False]))
    field.append(box((6, 7), [False, False, False, False]))
    field.append(box((6, 8), [True, True, False, False]))
    field.append(box((7, 0), [False, False, False, True]))
    field.append(box((7, 1), [False, False, False, False]))
    field.append(box((7, 2), [False, False, False, False]))
    field.append(box((7, 3), [False, False, True, False]))
    field.append(box((7, 4), [True, False, True, False]))
    field.append(box((7, 5), [False, False, True, False]))
    field.append(box((7, 6), [False, False, False, False]))
    field.append(box((7, 7), [False, False, False, False]))
    field.append(box((7, 8), [False, True, False, False]))
    field.append(box((8, 0), [False, False, True, True]))
    field.append(box((8, 1), [False, False, True, False]))
    field.append(box((8, 2), [False, True, True, False]))
    field.append(box((8, 6), [False, False, True, True]))
    field.append(box((8, 7), [False, False, True, False]))
    field.append(box((8, 8), [False, True, True, False]))
    fields.append(field)
    field = list()
    field.append(box((0, 0), [True, False, False, True]))
    field.append(box((0, 1), [True, False, False, False]))
    field.append(box((0, 2), [True, True, False, False]))
    field.append(box((0, 4), [True, False, False, True]))
    field.append(box((0, 5), [True, False, False, False]))
    field.append(box((0, 6), [True, True, False, False]))
    field.append(box((1, 0), [False, False, False, True]))
    field.append(box((1, 1), [False, False, False, False]))
    field.append(box((1, 2), [False, False, False, False]))
    field.append(box((1, 3), [True, False, False, False]))
    field.append(box((1, 4), [False, False, False, False]))
    field.append(box((1, 5), [False, False, True, False]))
    field.append(box((1, 6), [False, True, True, False]))
    field.append(box((2, 0), [False, False, False, True]))
    field.append(box((2, 1), [False, False, False, False]))
    field.append(box((2, 2), [False, False, True, False]))
    field.append(box((2, 3), [False, False, False, False]))
    field.append(box((2, 4), [False, True, False, False]))
    field.append(box((3, 0), [False, False, True, True]))
    field.append(box((3, 1), [False, True, True, False]))
    field.append(box((3, 3), [False, False, False, True]))
    field.append(box((3, 4), [False, False, False, False]))
    field.append(box((3, 5), [True, False, False, False]))
    field.append(box((3, 6), [True, False, False, False]))
    field.append(box((3, 7), [True, True, False, False]))
    field.append(box((4, 3), [False, False, False, True]))
    field.append(box((4, 4), [False, False, False, False]))
    field.append(box((4, 5), [False, False, True, False]))
    field.append(box((4, 6), [False, False, False, False]))
    field.append(box((4, 7), [False, True, True, False]))
    field.append(box((5, 0), [True, False, False, True]))
    field.append(box((5, 1), [True, True, False, False]))
    field.append(box((5, 3), [False, False, False, True]))
    field.append(box((5, 4), [False, True, True, False]))
    field.append(box((5, 6), [False, True, False, True]))
    field.append(box((6, 0), [False, False, False, True]))
    field.append(box((6, 1), [False, False, False, False]))
    field.append(box((6, 2), [True, False, False, False]))
    field.append(box((6, 3), [False, True, False, False]))
    field.append(box((6, 6), [False, False, False, True]))
    field.append(box((6, 7), [True, False, False, False]))
    field.append(box((6, 8), [True, True, False, False]))
    field.append(box((7, 0), [False, False, False, True]))
    field.append(box((7, 1), [False, False, False, False]))
    field.append(box((7, 2), [False, False, True, False]))
    field.append(box((7, 3), [False, False, False, False]))
    field.append(box((7, 4), [True, True, False, False]))
    field.append(box((7, 6), [False, False, False, True]))
    field.append(box((7, 7), [False, False, False, False]))
    field.append(box((7, 8), [False, True, False, False]))
    field.append(box((8, 0), [False, False, True, True]))
    field.append(box((8, 1), [False, True, True, False]))
    field.append(box((8, 3), [False, False, True, True]))
    field.append(box((8, 4), [False, True, True, False]))
    field.append(box((8, 6), [False, False, True, True]))
    field.append(box((8, 7), [False, False, True, False]))
    field.append(box((8, 8), [False, True, True, False]))
    fields.append(field)
    field = list()
    field.append(box((0, 0), [True, False, False, True]))
    field.append(box((0, 1), [True, False, False, False]))
    field.append(box((0, 2), [True, False, False, False]))
    field.append(box((0, 3), [True, False, False, False]))
    field.append(box((0, 4), [True, False, False, False]))
    field.append(box((0, 5), [True, False, False, False]))
    field.append(box((0, 6), [True, False, False, False]))
    field.append(box((0, 7), [True, False, False, False]))
    field.append(box((0, 8), [True, True, False, False]))
    field.append(box((1, 0), [False, False, True, True]))
    field.append(box((1, 1), [False, False, True, False]))
    field.append(box((1, 2), [False, False, True, False]))
    field.append(box((1, 3), [False, False, True, False]))
    field.append(box((1, 4), [False, False, True, False]))
    field.append(box((1, 5), [False, False, True, False]))
    field.append(box((1, 6), [False, False, True, False]))
    field.append(box((1, 7), [False, False, False, False]))
    field.append(box((1, 8), [False, True, False, False]))
    field.append(box((2, 7), [False, False, False, True]))
    field.append(box((2, 8), [False, True, False, False]))
    field.append(box((3, 0), [True, False, False, True]))
    field.append(box((3, 1), [True, False, False, False]))
    field.append(box((3, 2), [True, False, False, False]))
    field.append(box((3, 3), [True, False, False, False]))
    field.append(box((3, 4), [True, False, False, False]))
    field.append(box((3, 5), [True, True, False, False]))
    field.append(box((3, 7), [False, False, False, True]))
    field.append(box((3, 8), [False, True, False, False]))
    field.append(box((4, 0), [False, False, False, True]))
    field.append(box((4, 1), [False, False, False, False]))
    field.append(box((4, 2), [False, False, True, False]))
    field.append(box((4, 3), [False, False, False, False]))
    field.append(box((4, 4), [False, False, False, False]))
    field.append(box((4, 5), [False, True, False, False]))
    field.append(box((4, 7), [False, False, False, True]))
    field.append(box((4, 8), [False, True, False, False]))
    field.append(box((5, 0), [False, False, False, True]))
    field.append(box((5, 1), [False, True, False, False]))
    field.append(box((5, 3), [False, False, True, True]))
    field.append(box((5, 4), [False, False, True, False]))
    field.append(box((5, 5), [False, True, True, False]))
    field.append(box((5, 7), [False, False, False, True]))
    field.append(box((5, 8), [False, True, False, False]))
    field.append(box((6, 0), [False, False, False, True]))
    field.append(box((6, 1), [False, True, False, False]))
    field.append(box((6, 7), [False, False, False, True]))
    field.append(box((6, 8), [False, True, False, False]))
    field.append(box((7, 0), [False, False, False, True]))
    field.append(box((7, 1), [False, False, False, False]))
    field.append(box((7, 2), [True, False, False, False]))
    field.append(box((7, 3), [True, False, False, False]))
    field.append(box((7, 4), [True, False, False, False]))
    field.append(box((7, 5), [True, False, False, False]))
    field.append(box((7, 6), [True, False, False, False]))
    field.append(box((7, 7), [False, False, False, False]))
    field.append(box((7, 8), [False, True, False, False]))
    field.append(box((8, 0), [False, False, True, True]))
    field.append(box((8, 1), [False, False, True, False]))
    field.append(box((8, 2), [False, False, True, False]))
    field.append(box((8, 3), [False, False, True, False]))
    field.append(box((8, 4), [False, False, True, False]))
    field.append(box((8, 5), [False, False, True, False]))
    field.append(box((8, 6), [False, False, True, False]))
    field.append(box((8, 7), [False, False, True, False]))
    field.append(box((8, 8), [False, True, True, False]))
    fields.append(field)
    field = list()
    field.append(box((0, 2), [True, False, False, True]))
    field.append(box((0, 3), [True, True, False, False]))
    field.append(box((0, 7), [True, False, False, True]))
    field.append(box((0, 8), [True, True, False, False]))
    field.append(box((1, 2), [False, False, False, True]))
    field.append(box((1, 3), [False, False, False, False]))
    field.append(box((1, 4), [True, True, False, False]))
    field.append(box((1, 7), [False, False, False, True]))
    field.append(box((1, 8), [False, True, True, False]))
    field.append(box((2, 0), [True, False, False, True]))
    field.append(box((2, 1), [True, False, False, False]))
    field.append(box((2, 2), [False, False, False, False]))
    field.append(box((2, 3), [False, False, False, False]))
    field.append(box((2, 4), [False, True, True, False]))
    field.append(box((2, 7), [False, True, False, True]))
    field.append(box((3, 0), [False, False, False, True]))
    field.append(box((3, 1), [False, False, False, False]))
    field.append(box((3, 2), [False, False, False, False]))
    field.append(box((3, 3), [False, True, False, False]))
    field.append(box((3, 6), [True, False, False, True]))
    field.append(box((3, 7), [False, False, False, False]))
    field.append(box((3, 8), [True, True, False, False]))
    field.append(box((4, 0), [False, False, False, True]))
    field.append(box((4, 1), [False, False, False, False]))
    field.append(box((4, 2), [False, False, False, False]))
    field.append(box((4, 3), [False, False, False, False]))
    field.append(box((4, 4), [True, False, False, False]))
    field.append(box((4, 5), [True, False, True, False]))
    field.append(box((4, 6), [False, False, False, False]))
    field.append(box((4, 7), [False, False, False, False]))
    field.append(box((4, 8), [False, True, True, False]))
    field.append(box((5, 0), [False, False, True, True]))
    field.append(box((5, 1), [False, False, True, False]))
    field.append(box((5, 2), [False, False, True, False]))
    field.append(box((5, 3), [False, False, False, False]))
    field.append(box((5, 4), [False, True, False, False]))
    field.append(box((5, 6), [False, False, True, True]))
    field.append(box((5, 7), [False, True, True, False]))
    field.append(box((6, 3), [False, False, False, True]))
    field.append(box((6, 4), [False, True, False, False]))
    field.append(box((7, 2), [True, False, False, True]))
    field.append(box((7, 3), [False, False, False, False]))
    field.append(box((7, 4), [False, True, False, False]))
    field.append(box((7, 6), [True, False, False, True]))
    field.append(box((7, 7), [True, False, False, False]))
    field.append(box((7, 8), [True, True, False, False]))
    field.append(box((8, 2), [False, False, True, True]))
    field.append(box((8, 3), [False, False, True, False]))
    field.append(box((8, 4), [False, False, True, False]))
    field.append(box((8, 5), [True, False, True, False]))
    field.append(box((8, 6), [False, False, True, False]))
    field.append(box((8, 7), [False, False, True, False]))
    field.append(box((8, 8), [False, True, True, False]))
    fields.append(field)
    #return fields[7]
    #return fields[randint(0, len(fields)-1)]
    boolfield = [[False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False],
                 [False, False, False, False, False, False, False, False, False]]
    boolfield[randint(0,8)][randint(0,8)] = True
    field = generateField(boolfield)
    while (not isValid(field)) or isTooSmall(field) or allWalls(boolfield):
        if not isValid(field):
            pos = getNotValid(field)
            boolfield = addField(boolfield, pos)
            field = generateField(boolfield)
        elif allWalls(boolfield):
            pos = getAllWalls(boolfield)
            boolfield[pos[0]][pos[1]] = True
            field = generateField(boolfield)
        else:
            pos = getValidWithWall(field)
            boolfield = addField(boolfield, pos)
            field = generateField(boolfield)
    return field
    field = list()
    field.append(box((randint(0,8), randint(0,8)), [False, False, False, False]))

def generateField(boolfield):
    field = list()
    for i in range(9):
        for j in range(9):
            if boolfield[i][j]:
                if i == 0:
                    north = True
                else:
                    north = not boolfield[i-1][j]
                if j == 0:
                    west = True
                else:
                    west = not boolfield[i][j-1]
                if i == 8:
                    south = True
                else:
                    south = not boolfield[i+1][j]
                if j == 8:
                    east = True
                else:
                    east = not boolfield[i][j+1]
                field.append(box((i,j),[north, east, south, west]))
    return field

def isValid(field):
    for box in field:
        if box.getWallNumber() > 2:
            return False
    return True

def getNotValid(field):
    for box in field:
        if box.getWallNumber() > 2:
            return box.pos
    return None

def addField(boolfield, pos):
    possible = list()
    if pos[0] < 8 and not boolfield[pos[0]+1][pos[1]]:
        possible.append((pos[0]+1,pos[1]))
    if pos[0] > 0 and not boolfield[pos[0]-1][pos[1]]:
        possible.append((pos[0]-1,pos[1]))
    if pos[1] < 8 and not boolfield[pos[0]][pos[1]+1]:
        possible.append((pos[0],pos[1]+1))
    if pos[1] > 0 and not boolfield[pos[0]][pos[1]-1]:
        possible.append((pos[0],pos[1]-1))
    newPos = possible[randint(0,len(possible)-1)]
    boolfield[newPos[0]][newPos[1]] = True
    return boolfield

def isTooSmall(field):
    if len(field)<20:
        return True
    if len(field)<27:
        if not randint(0,5) == 0:
            return True
    if len(field)<34:
        if not randint(0,2) == 0:
            return True
    if len(field)<41:
        if not randint(0,1) == 0:
            return True
    if len(field)<48:
        if randint(0,2) == 0:
            return True
    if len(field)<55:
        if randint(0,4) == 0:
            return True
    if len(field)<62:
        if randint(0,10) == 0:
            return True
    if len(field)<69:
        if randint(0,100) == 0:
            return True
    return False

def getValidWithWall(field):
    possible = list()
    for box in field:
        i = box.getWallNumber()
        if box.pos[0] == 0 or box.pos[0] == 8:
            i -= 1
        if box.pos[1] == 0 or box.pos[1] == 8:
            i -= 1
        if i > 0:
            possible.append(box.pos)
    return possible[randint(0, len(possible) - 1)]

def allWalls(boolfield):
    for i in range(1,8):
        for j in range(1,8):
            if boolfield[i-1][j] and boolfield[i+1][j] and boolfield[i][j+1] and boolfield[i][j-1] and not boolfield[i][j]:
                return True
    return False

def getAllWalls(boolfield):
    for i in range(1,8):
        for j in range(1,8):
            if boolfield[i-1][j] and boolfield[i+1][j] and boolfield[i][j+1] and boolfield[i][j-1] and not boolfield[i][j]:
                return (i,j)

def printField(boolfield):
    for i in boolfield:
        text = ""
        for j in i:
            if j:
                text += "X"
            else:
                text += " "
        print(text)