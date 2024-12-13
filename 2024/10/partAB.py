import datetime

startTime = datetime.datetime.now()

mapa = [list(l.replace("\n","")) for l in open("myinput").readlines()]
for r in range(len(mapa)):
    for c in range(len(mapa)):
        try:
            mapa[r][c] = int(mapa[r][c])
        except ValueError as e:
            mapa[r][c] = -1


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

lc = len(mapa[0])
lr = len(mapa[0])
def inMap(r, c):
    return ( r >= 0) and (c>=0) and (c<lc) and (r < lr)

nextSteps =[
    ( 1, 0),
    ( 0, 1),
    (-1, 0),
    (0, -1)
]

def runTrail(mapa, start):
    startValue = mapa[start[0]][start[1]]

    if startValue == 9:
        return [start]

    validTrails = []
    for d in nextSteps:
        newStep = (start[0] + d[0], start[1] + d[1])
        if inMap(newStep[0], newStep[1]):
            if mapa[newStep[0]][newStep[1]] == startValue + 1:
                valids = runTrail(mapa, newStep)
                validTrails += valids

    return validTrails


scores = 0
scoresB = 0
for r in range(len(mapa)):
    for c in range(len(mapa)):
        if mapa[r][c] == 0:
            ret = runTrail(mapa, (r, c))
            scoresB += len(ret)
            scores += len(set(ret))

b = datetime.datetime.now()
print(f"Result: {scores}")
print(f"ResultB: {scoresB}")
print(f"Time: {(b-startTime).microseconds}")
