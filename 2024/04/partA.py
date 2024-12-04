import re
import numpy as np

letters = open("myinput","r").readlines()
#letters = open("test","r").readlines()
letters = [list(l.replace("\n","")) for l in letters]

def checkInRange(i,j):
    return (i < len(letters[0])) and (j < len(letters)) and i >= 0 and j >= 0

def checkDiag(ox, oy, dir):
    global letters
    word = "XMAS"

    for i in range(len(word)):
        newI = ox + dir[0]*i
        newJ = oy + dir[1]*i
        if not checkInRange(newI, newJ):
            return 0
        # SE
        if letters[newI][newJ] != word[i]:
            return 0
    print(f"Found diag {ox, oy} dir {dir}")
    return 1



reXmas=r"XMAS"
hor = 0
nHor = 0
for r in letters:
    hor += len(re.findall(reXmas, "".join(r)))
    nHor += len(re.findall(reXmas, "".join(reversed(r))))
print(f"Horizontales normales {hor}")
print(f"Horizontales al reves {nHor}")

tLetters = np.transpose(letters)
ver = 0
nVer = 0
for r in tLetters:
    ver += len(re.findall(reXmas, "".join(r)))
    nVer += len(re.findall(reXmas, "".join(reversed(r))))

diags = 0
for i in range(len(letters)):
    for j in range(len(letters)):
        diags += checkDiag(i,j, [1,1])
        diags +=checkDiag(i,j, [1,-1])
        diags +=checkDiag(i,j, [-1,1])
        diags +=checkDiag(i,j, [-1,-1])

print(f"Verticales normales {ver}")
print(f"Verticales al reves {nVer}")

print(f"Total {hor + nHor + ver + nVer + diags}")


