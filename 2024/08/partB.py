import itertools
import datetime

a = datetime.datetime.now()
lines = [list(l.replace("\n","")) for l in open("myinput","r").readlines()]


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


ant = {}
for r in range(len(lines)):
    for c in range(len(lines[r])):
        char =  lines[r][c]
        if char != ".":
            if not char in ant.keys():
                ant[char] = []
            ant[char].append((c, r))

def inMap(x,y, map):
    return ( x >= 0) and (y>=0) and (x<len(map[0])) and (y < len(map))

def calculateAntinode(posA, posB):
    dx = (posB[0]-posA[0])
    dy = (posB[1]-posA[1])
    return (posB[0]+dx, posB[1]+dy)


mapa = lines.copy()
count = 0
for k in ant.keys():
    for x in itertools.product(ant[k], repeat=2):
        if x[0] == x[1]:
            continue

        pos = [x[0], x[1]]

        anti = calculateAntinode(pos[0], pos[1])

        if mapa[x[0][1]][x[0][0]] != "#":
            mapa[x[0][1]][x[0][0]] = "#"
            count += 1
        
        if mapa[x[1][1]][x[1][0]] != "#":
            mapa[x[1][1]][x[1][0]] = "#"
            count += 1

        while inMap(anti[0], anti[1], mapa):
            if mapa[anti[1]][anti[0]] != "#":
                mapa[anti[1]][anti[0]] = "#"
                count += 1
            
            pos = [pos[1], anti]
            anti = calculateAntinode(pos[0], pos[1])

print(count)
b = datetime.datetime.now()

print(f"Time: {(b-a).microseconds}")