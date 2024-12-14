import re
import numpy as np
from PIL import Image


LEN_X = 101
LEN_Y = 103

robots = []
linere = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
for l in open("myinput").readlines():
    res = re.match(linere, l) 
    pos = (int(res.group(1)), int(res.group(2)))
    vel = (int(res.group(3)), int(res.group(4)))
    robots.append((pos, vel))


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

OFFSET = 7000
img = Image.new( 'L', (LEN_X, LEN_Y))
mapa = np.array(img)
for i in range(1000):
    for y in range(LEN_Y):
        for x in range(LEN_X):
            mapa[y][x] = 0
    for r in robots:
        p = getRobotPos(r, i+OFFSET)
        mapa[p[1]][p[0]] = 255
    
    Image.fromarray(mapa).save(f'images/day14-{i+OFFSET}.png')
    print(i+OFFSET)


safety = 1
for q in quadrants.values():
    safety *= q

print(f"Safety: {safety}")

