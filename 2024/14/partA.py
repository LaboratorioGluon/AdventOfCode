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
        print(str(i) + " ", end="")
    print()
    cnt = 0
    for i in m:
        print(str(cnt)+" ", end = "")
        cnt += 1
        for j in i:
            print(str(j)+ " ", end="")
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

for r in robots:
    p = getRobotPos(r, 100)
    if p[0] != midX and p[1] != midY:
        quadrants[ (p[0] < midX, p[1] < midY) ] += 1

safety = 1
for q in quadrants.values():
    safety *= q

print(f"Safety: {safety}")

