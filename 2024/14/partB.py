import re

LEN_X = 101
LEN_Y = 103

robots = []
linere = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
for l in open("myinput").readlines():
    res = re.match(linere, l) 
    pos = (int(res.group(1)), int(res.group(2)))
    vel = (int(res.group(3)), int(res.group(4)))
    robots.append((pos, vel))

def debugPrint(m):
    print("  ", end="")
    for i in range(len(m[0])):
        print(str(i) + "", end="")
    print()
    cnt = 0
    for i in m:
        print(str(cnt)+"", end = "")
        cnt += 1
        for j in i:
            print(str(j)+ "", end="")
        print()


def getRobotPos(robot, secs):
    p = robot[0]
    v = robot[1]
    return ((p[0]+secs*v[0])%LEN_X, (p[1]+secs*v[1])%LEN_Y)


quadrants = {
    (False, False): 0,
    (False, True):  0,
    (True, False): 0,
    (True, True ): 0
}

midX = LEN_X//2
midY = LEN_Y//2
print(midX)
print(midY)
mapa = []
for y in range(LEN_Y):
    mapa.append([])
    for x in range(LEN_X):
        mapa[y].append(' ')

OFFSET = 7000
for i in range(1000):
    for y in range(LEN_Y):
        for x in range(LEN_X):
            mapa[y][x] = " "
    for r in robots:
        p = getRobotPos(r, i+7000)
        mapa[p[1]][p[0]] = "#"
    debugPrint(mapa)
    print(i+7000)


safety = 1
for q in quadrants.values():
    safety *= q

print(f"Safety: {safety}")

