import re
import numpy as np

def parseFile(file):
    blockre = r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)"""

    lines = open(file).read()
    res = re.findall(blockre, lines)
    blocks = []
    
    for r in res:
        r = [int(x) for x in r]
        eqs = np.array([[r[0], r[2]], [r[1], r[3]]])
        sol = np.array([r[4], r[5]])
        blocks.append((eqs, sol))
    return blocks


test = parseFile("myinput")

price = 0
for t in test:
    solution = np.linalg.solve(t[0], t[1])
    nSol = [np.round(x) for x in solution]
    asol = [int(x) for x in np.dot(t[0], nSol)]
    if asol[0] >= 0 and asol[1]>= 0 and asol[0] == t[1][0] and asol[1] == t[1][1]:
        price += nSol[0]*3 + nSol[1]

print(price)

