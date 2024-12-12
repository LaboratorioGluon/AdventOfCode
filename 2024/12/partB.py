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

def inMap2(r,c, map):
    return (( r >= 0) and (r < len(map[0])), ( (c >= 0) and (c < len(map))))

def getMap(mapa, pos):
    if inMap(pos[0], pos[1], mapa):
        return mapa[pos[0]][pos[1]]
    else:
        return None

def setMap(mapa, pos, value):
    mapa[pos[0]][pos[1]] = value

nextSteps =[
    ( 1, 0),
    ( 0, 1),
    (-1, 0),
    (0, -1)
]


def move(a, dir):
    return ([a[0] + dir[0], a[1] + dir[1]], dir)

def getArea(pMapa, start, ppVisited):
    name = getMap(pMapa, start)
    
    field = [start]

    fences = 0
    sides = 0


    pVisited = copy.deepcopy(pMapa)
    setMap(pVisited, start, '.')
    visited = []

    toCheck = [start]

    while len(toCheck) > 0:
        pos = toCheck.pop(0)
        neig = [move(pos,d) for d in nextSteps]
        #print(f"Checking {pos} -> {neig}")
        for n in neig:
            coord = n[0]
            dd = n[1]

            nValue = getMap(pMapa, n[0])

            if getMap(pVisited, coord) == ".": # Already visited
            #if coord in visited:
                pass
            elif nValue == name:
                #Inside field
                field.append(coord.copy())
                toCheck.append(coord.copy())
                setMap(pVisited, coord, ".")
                setMap(ppVisited, coord, ".")
                visited.append(coord)
            else:
                #Outside
                fences += 1

                rotated = [pos[0] - dd[1], pos[1] +  dd[0]]
            
                #print(f"Corner in {pos} {rotated}")
                #print(f" - {getMap(pMapa, rotated)} -> {getMap(pMapa, rotated) != name}")
                #print(f" - {getMap(pMapa, [rotated[0] + dd[0], rotated[1] + dd[1]])} -> {getMap(pMapa, [rotated[0] + dd[0], rotated[1] + dd[1]]) == name}")
                if getMap(pMapa, rotated) != name or getMap(pMapa, [rotated[0] + dd[0], rotated[1] + dd[1]]) == name:
                    sides += 1
                    
                    
    #debugPrint(pVisited)
    #print(f"Fences {fences}, sides {sides}, area{len(field)}")
    #ppVisited = copy.deepcopy(pVisited)
    #input()
    return (fences, field, sides)
    

visited = copy.deepcopy(gmapa)
total = 0
toDebug = False
for r in range(len(gmapa)):
    for c in range(len(gmapa[0])):
        if visited[r][c] != '.':
            prev = gmapa[r][c] 
            f, ff, sides= getArea(copy.deepcopy(gmapa), [r,c], visited)
            total += len(ff) * sides

print(total)