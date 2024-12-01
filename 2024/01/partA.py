import numpy as np

# Test lines
lines = """3 4
4 3
2 5
1 3
3 9
3 3""".split("\n")

lines = [ l.replace("\n","").split() for l in open("myinput","r").readlines()] 
#lines = [ l.replace("\n","").split() for l in lines] 

data = [[int(l[0]), int(l[1])] for l in lines]
data = np.transpose(data)

sortedA = sorted(data[0])
sortedB = sorted(data[1])

print(np.sum(np.abs(np.subtract(sortedA, sortedB))))
