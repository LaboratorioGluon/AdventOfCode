import re

mulre = r'mul\((\d{1,3},\d{1,3})\)'

#line = open('test','r').read()
line = open('myinput','r').read()

res = re.findall(mulre, line)

suma = 0
for r in res:
    suma += int(r.split(",")[0])* int(r.split(",")[1])

print(suma)

