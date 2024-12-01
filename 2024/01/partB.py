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

output = []
for d in data[0]:
    output.append(d*(data[1] == d).sum())

print(np.sum(output))

