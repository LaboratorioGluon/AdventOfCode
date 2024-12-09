#line = open("test","r").readlines()[0].replace("\n","")
line = open("myinput","r").readlines()[0].replace("\n","")


def prepareDisk(blocks):
    currentId = 0
    disk = []
    isFile = True
    for b in blocks:
        for i in range(int(b)):
            if isFile:
                disk.append(currentId)
            else:
                disk.append(None)
        isFile = not isFile
        if isFile:
            currentId += 1
    return disk

def searchNextNone(blocks, prevNone = 0):
    if None in blocks[prevNone+1:]:
        return blocks[prevNone+1:].index(None)+prevNone+1
    else:
        return None


disk = prepareDisk(line)

print(len(disk))
noneIndex = searchNextNone(disk, 0)
for i in range(len(disk)):
    if disk[len(disk)-i-1] != None:
        if len(disk)-i-1 < noneIndex:
            break
        disk[noneIndex] = disk[len(disk)-i-1]
        disk[len(disk)-i-1] = None
        newNoneIndex = searchNextNone(disk, noneIndex)
        noneIndex = newNoneIndex


suma = 0
for i in range(len(disk)):
    if disk[i] == None:
        break
    suma += disk[i]*i

print(suma)
    
    