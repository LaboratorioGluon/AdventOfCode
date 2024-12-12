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
    return ([a[0] + dir[0], a[1] + dir[1]], dir, a)

def getArea(pMapa, start, pVisited):
    name = getMap(pMapa, start)
    
    setMap(pMapa, start, '.')
    toCheck = [move(start,d) for d in nextSteps]
    fence = 0
    field = [start]
    fencesHU = []
    fencesHD = []
    fencesVL = []
    fencesVR = []
    while len(toCheck) > 0:
        pos = toCheck[0][0]
        currDir = toCheck[0][1]
        prev = toCheck[0][2]
        #print(f"Checking {pos}")
        inm = inMap2(pos[0], pos[1], pMapa)
        if not all(inm):
            fence += 1
            if inm[0] == False:
                if dir[1] == -1:
                    fencesVR.append(pos)
                else:
                    fencesVL.append(pos)
            else:
                if dir[0] == -1:
                    fencesHU.append(pos)
                else:
                    fencesHD.append(pos)

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
                if currDir[1] == 0:
                    if currDir[0] == 1:
                        fencesHD.append(pos)
                    else:
                        fencesHU.append(pos)
                else:
                    if currDir[1] == 1:
                        fencesVR.append(pos)
                    else:
                        fencesVL.append(pos)
        toCheck.pop(0)
    
    if name != None:
        debugPrint(pMapa)
        print(f"Horizontales: {fencesHU} \n {fencesHD}")
        print(f"Verticales: {fencesVR} \n {fencesVL}")
    return (fence, field, fencesHU, fencesHD, fencesVR, fencesVL)
    
"""Legacy try: Abandoned just FYI"""
"""
def getFenceSides(fences, debug=False):

    def extractConsecutives(l:list):
        val = l.pop(0)
        while True:
            for i in l:
                if i == val + 1:
                    val = i
                    l.pop(l.index(val))
                    break
            else:
                break

    diccs = []
    for f in fences:
        diccs.append({})
        for fi in f:
            if not fi in diccs[-1]:
                diccs[-1][fi][0]
    
    for h in diccs[0].keys():
        diccs[0][h]


    for r in rg.keys():
        rg[r] = [x for _, x in sorted(rg[r], key = lambda x: x[1])]

    for c in cg.keys():
        cg[c] = [x for x, _ in sorted(cg[c], key = lambda x: x[0])]

    if True:
        print(f"Rows: {rg}")
        print(f"Cols: {cg}")

    sides = 0
    for r in rg.keys():
        while len(rg[r]) > 0:
            print(rg[r])
            extractConsecutives(rg[r])
            sides += 1
    for c in cg.keys():
        while len(cg[c]) > 0:
            print(cg[c])
            extractConsecutives(cg[c])
            sides += 1

    print(sides)
    return sides


    trozos = 0
    lastTrozo = []
    for r in rg.keys():
        #print(f"Row: {r}")
        lastc = rg[r][0][1]
        #trozos+=1
        for i in rg[r]:
            #print(f"{i} {i[1] - lastc}")
            if i - lastc > 1:
                #print("Nuevo trozo")
                trozos += 1
                print(lastTrozo)
                lastTrozo = []
                
            elif i == lastc:
                #print("Nuevo trozo")
                print(lastTrozo)
                lastTrozo = []
                trozos += 1
            lastTrozo.append(i)
            lastc = i
    print("..")
    for g in cg.keys():
        #print(f"Col: {c}")
        #lastc = cg[g][0][0]
        #trozos+=1
        trozos = 1

        for i in cg[g]:
            #print(f"{i} {i[0] - lastc}")
            if i - lastc > 1:
                #print("Nuevo trozo")
                trozos += 1
                print(lastTrozo)
                lastTrozo = []
            lastTrozo.append(i)
            lastc = i
    print(lastTrozo)

    return trozos
"""

#debugPrint(gmapa)

visited = copy.deepcopy(gmapa)
total = 0
toDebug = False
for r in range(len(gmapa)):
    for c in range(len(gmapa[0])):
        if visited[r][c] != '.':
            prev = gmapa[r][c] 
            f, ff, fch, fcv = getArea(copy.deepcopy(gmapa), [r,c], visited)
            #total += f*len(ff)
            if visited[r][c] == 'V':
                toDebug = False
            else:
                toDebug = False
            tr = getFenceSides(fch, fcv, debug=toDebug)
            #print(f"Price: {len(ff)} x {tr}")
            print(tr)
            total += len(ff) * tr
            input()

print(total)