#line = open("test","r").readlines()[0].replace("\n","")
line = open("myinput","r").readlines()[0].replace("\n","")

emptyBlocksInfo = []
emptyBlocksSizes = []
fileBlocksInfo = []
fileBlocksSizes = []

def prepareDisk(blocks):

    currentBlockIndex = 0
    currentId = 0
    disk = []
    isFile = True
    for b in blocks:

        if isFile:
            fileBlocksSizes.append(int(b))
            fileBlocksInfo.append((currentBlockIndex, currentId))
        else:
            emptyBlocksSizes.append(int(b))
            emptyBlocksInfo.append(currentBlockIndex)

        for i in range(int(b)):
            if isFile:
                disk.append(currentId)
            else:
                disk.append(None)
            
            currentBlockIndex += 1
        isFile = not isFile
        if isFile:
            currentId += 1
    return disk


def fillEmptyBlock(disk, emptyBlockIndex, fileBlockIndex):
    start = emptyBlocksInfo[emptyBlockIndex]
    size = fileBlocksSizes[fileBlockIndex]
    end = start + size

    # Fill disk with ID
    disk[start:end] = [fileBlocksInfo[fileBlockIndex][1]]*(size)
    emptyBlocksInfo[emptyBlockIndex] = emptyBlocksInfo[emptyBlockIndex] + size
    emptyBlocksSizes[emptyBlockIndex] = emptyBlocksSizes[emptyBlockIndex] - size

    # Clear old ID
    start = fileBlocksInfo[fileBlockIndex][0]
    size = fileBlocksSizes[fileBlockIndex]
    end = start + size
    disk[start:end] = [None]*(size)



disk = prepareDisk(line)
print(len(disk))


cnt = 0
for i in range(len(fileBlocksSizes)):
    fileIndex = len(fileBlocksSizes)-1-i
    blockLen = fileBlocksSizes[fileIndex]
    for eindex in range(len(emptyBlocksSizes)):
        if fileBlocksInfo[fileIndex][0] < emptyBlocksInfo[eindex]:
            break
        if emptyBlocksSizes[eindex] >= blockLen:
            fillEmptyBlock(disk, eindex, fileIndex)
            break

suma = 0
for i in range(len(disk)):
    if disk[i] != None:
        suma += disk[i]*i
        
print(suma)
    
    