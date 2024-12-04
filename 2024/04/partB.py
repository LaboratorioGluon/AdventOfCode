import re
import numpy as np

letters = open("myinput","r").readlines()
#letters = open("test","r").readlines()
letters = [list(l.replace("\n","")) for l in letters]

def checkInRange(i,j):
    return (i < len(letters[0])) and (j < len(letters)) and i >= 0 and j >= 0

def checkDiag(ox, oy, dir, deep=0):
    global letters
    word = "MAS"
    
    nox = ox - dir[0]
    noy = oy - dir[1]
    
    for i in range(len(word)):
        newI = nox + dir[0]*i
        newJ = noy + dir[1]*i
        if not checkInRange(newI, newJ):
            return 0
        # SE
        if letters[newI][newJ] != word[i]:
            return 0
    d1 = True
    d2 = True
    if not deep:
        d1 = checkDiag(ox,oy,[dir[0], -dir[1]],1)
        d2 = checkDiag(ox,oy,[-dir[0], dir[1]],1)
    if (d1 or d2) and deep == 0:
        print(f"Found diag {ox, oy} dir {dir}, {d1},{d2}, {deep}")
    return d1 or d2


diags = 0
for i in range(len(letters)):
    for j in range(len(letters)):
        diags += checkDiag(i,j, [1,1])
        diags += checkDiag(i,j, [-1,-1])

print(f"Total:  {diags}")