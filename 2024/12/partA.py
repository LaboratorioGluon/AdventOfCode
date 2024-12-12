import copy

gmapa = [list(l.replace("\n","")) for l in open("myinput").readlines()]


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

def inMap(r,c, map):
    return ( r >= 0) and (c >= 0) and (r < len(map[0])) and (c < len(map))

def getMap(mapa, pos):
    return mapa[pos[0]][pos[1]]

def setMap(mapa, pos, value):
    mapa[pos[0]][pos[1]] = value

nextSteps =[
    ( 1, 0),
    ( 0, 1),
    (-1, 0),
    (0, -1)
]

def move(a, dir):
    return [a[0] + dir[0], a[1] + dir[1]]

def getArea(pMapa, start, pVisited):
    name = getMap(pMapa, start)
    
    setMap(pMapa, start, '.')
    toCheck = [move(start,d) for d in nextSteps]
    fence = 0
    field = [start]
    while len(toCheck) > 0:
        pos = toCheck[0]
        #print(f"Checking {pos}")
        if not inMap(pos[0], pos[1], pMapa):
            fence += 1
        else:
            newPosName = getMap(pMapa, pos)
            if newPosName == name:
                #print(f"Adding {pos}")
                field.append(pos)
                toCheck += [move(pos,d) for d in nextSteps]
                setMap(pMapa, pos, '.')
                setMap(pVisited, pos , '.')
            elif newPosName == ".":
                pass
            else:
                fence += 1
        toCheck.pop(0)
    return (fence, field)
    

#debugPrint(gmapa)

visited = copy.deepcopy(gmapa)
total = 0
for r in range(len(gmapa)):
    for c in range(len(gmapa[0])):
        if visited[r][c] != '.':
            prev = gmapa[r][c] 
            f, ff = getArea(copy.deepcopy(gmapa), [r,c], visited)
            total += f*len(ff)
            #print(f" For {prev} -> {f} {len(ff)}")
            #debugPrint(visitedMap)
print(total)