
mapa = [list(m) for m in [l.replace("\n","") for l in open("test","r").readlines()]]
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
            print(j+ " ", end="")
        print()

debugPrint(mapa)

visited = mapa.copy()
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
        if not isValidCoord(mapa, nextCellCoord):
            exitZone = True
            break
        nextCell = mapa[nextCellCoord[0]][nextCellCoord[1]]
        #print(nextCellCoord)
    return listOfCells, exitZone



pos = startingPos
cells, exitZone = moveToNext(mapa, pos, dir)
for c in cells:
    visited[c[0]][c[1]] = "X"
#debugPrint(visited)

pos = cells[-1]
dir = nextDir(dir)
while pos != startingPos or dir != (-1, 0) :
    cells, exitZone = moveToNext(mapa, pos, dir)
    for c in cells:
        visited[c[0]][c[1]] = "X"
        if (c,dir) in visitedList:
            break
        visitedList.append( (c, dir) )
    #debugPrint(visited)

    if exitZone:
        print("Ha salido...")
        break
    pos = cells[-1]
    dir = nextDir(dir)



Xs = 0
for i in range(len(mapa)):
    for j in range(len(mapa[0])):
        if visited[i][j] == "X":
            Xs += 1
print(Xs)