import copy

import line_profiler

#mapa = [list(m) for m in [l.replace("\n","") for l in open("test","r").readlines()]]
mapa = [list(m) for m in [l.replace("\n","") for l in open("myinput","r").readlines()]]

def debugPrint(m):
    print("  ", end="")
    for i in range(len(m[0])):
        print(str(i) + " ", end="")
    print()
    cnt = 0
    for i in m:
        print(str(cnt)+" ", end = "")
        cnt += 1
        for j in i:
            print(str(j)+ " ", end="")
        print()

#debugPrint(mapa)

visited = copy.deepcopy(mapa)
visitedList = []

for i in range(len(mapa)):
    for j in range(len(mapa[0])):
        if mapa[i][j] == "^":
            startingPos = (i, j)

# Todas los ejes son: ( filas creciente hacia abajo , columna creciente derecha)
dir = (-1 , 0)
print(startingPos)

def move(p, d):
    return ( p[0] + d[0], p[1] + d[1])

def isValidCoord(mapa, pos):
    if (pos[0] < 0) or (pos[0] >= len(mapa)):
        return False
    if (pos[1] < 0) or (pos[1] >= len(mapa[0])):
        return False
    return True

def nextDir(dir):
    next = {
        (-1, 0): (0,  1),
        ( 0, 1): (1,  0),
        ( 1, 0): (0, -1),
        ( 0,-1): (-1, 0)
    }
    nextDir = next[dir]
    return nextDir

# Ret: Indices por donde ha pasado.
def moveToNext(mapa, pos, dir):
    exitZone = False
    listOfCells = [pos]
    nextCellCoord = move(pos, dir)
    nextCell = mapa[nextCellCoord[0]][nextCellCoord[1]]
    while nextCell != "#" :
        listOfCells.append(nextCellCoord)
        nextCellCoord = move(nextCellCoord, dir)
        #nextCellCoord = (nextCellCoord[0] + dir[0], nextCellCoord[1] + dir[1])
        if not isValidCoord(mapa, nextCellCoord):
            exitZone = True
            break
        nextCell = mapa[nextCellCoord[0]][nextCellCoord[1]]
        #print(nextCellCoord)
    return listOfCells, exitZone

localVisitedList = [ []*len(mapa[0]) for i in range(len(mapa)) ]

for i in range(len(mapa)):
    #localVisitedList[i] = 
    for j in range(len(mapa[0])):
        localVisitedList[i].append([])

@line_profiler.profile
def guardRun(mapa, pos, dir):
    isLoop = False

    visited = [ [j for j in mapa[i]]for i in range(len(mapa)) ]
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            localVisitedList[i][j] = []
    onlyvisitedList = []
    pos = startingPos
    """cells, exitZone = moveToNext(mapa, pos, dir)
    for c in cells[:-1]:
        visited[c[0]][c[1]] = "X"
        if not dir in localVisitedList[c[0]][c[1]]:
            localVisitedList[c[0]][c[1]].append(dir)
        #localVisitedList.append( c+dir )
        onlyvisitedList.append(c)
    """

    #pos = cells[-1]
    #dir = nextDir(dir)
    while not isLoop :
        cells, exitZone = moveToNext(mapa, pos, dir)
        for c in cells:
            #print(c)
            visited[c[0]][c[1]] = "X"
            if dir in localVisitedList[c[0]][c[1]]:
                isLoop = True
                """print("En loop:")
                print(localVisitedList[c[0]][c[1]])
                debugPrint(localVisitedList)
                debugPrint(visited)
                input()"""
                break
            if not dir in localVisitedList[c[0]][c[1]]:
                #print(f"Added {dir} at {c[0]}, {c[1]}")
                localVisitedList[c[0]][c[1]].append(dir)
                #debugPrint(localVisitedList)
            onlyvisitedList.append(c)
        #debugPrint(visited)

        if exitZone:
            break
        pos = cells[-1]
        dir = nextDir(dir)
    #debugPrint(visited)
    return isLoop, onlyvisitedList, visited

#debugPrint(mapa)

countLoops = 0
cnt = 0
mapa2 = copy.deepcopy(mapa)
previj = (0,0)
print(startingPos)
_, localVisited, _ = guardRun(mapa, startingPos, dir)
print(localVisited)
print(f"Len {len(localVisited)}")

loopsCoords = []
cntotal = 0
for vis in localVisited:
    #print(vis)
    i = vis[0]
    j = vis[1]
    if (i,j) != startingPos:
        mapa2[i][j] = "#"
        
        isLoop, visitedList2, _ = guardRun(mapa2, startingPos, dir)

        mapa2[i][j] = mapa[i][j]
        if isLoop and not (i,j) in loopsCoords:
            loopsCoords.append((i,j))

print(len(loopsCoords))
