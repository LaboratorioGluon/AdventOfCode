import itertools

data = [l.replace("\n","").split(": ") for l in open("myinput","r").readlines()]

def runOperations(elem: list, op:list):
    res = elem[0]
    for i in range(len(op)):
        if op[i] == 0:
            res += elem[i+1]
        elif op[i] == 1:
            res *= elem[i+1]
    
    return res

# operation 0 = ADD
# operation 1 = PRODUCT
operations = [0, 1]

solution = 0
for line in data:
    target = int(line[0])
    values = [int(a) for a in line[1].split(" ")]
    for c in list(itertools.product(operations, repeat=len(values)-1)):
        result = runOperations(values, c)
        if result == target:
            solution += result
            break

print(solution)
