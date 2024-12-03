import re

mulre = r'mul\((\d{1,3},\d{1,3})\)'

#line = open('test2','r').read()
line = open('myinput','r').read()

def runmul(line):
    res = re.findall(mulre, line)
    suma = 0
    for r in res:
        suma += int(r.split(",")[0])* int(r.split(",")[1])
    return suma

dos = line.split("do()")
sum = 0
for d in dos:
    donts = d.split("don't()")
    sum += runmul(donts[0])

print(sum)