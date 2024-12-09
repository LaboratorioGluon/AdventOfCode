import itertools

import line_profiler

data = [l.replace("\n","").split(": ") for l in open("myinput","r").readlines()]


@line_profiler.profile
def runOperations(elem: list, op:list, target: int):
    res = elem[0]
    for i in range(len(op)):
        if op[i] == 0:
            res += elem[i+1]
        elif op[i] == 1:
            res *= elem[i+1]
        elif op[i] == 2:
            res = res*(10**len(str(elem[i+1]))) + elem[i+1]
        if res > target:
            return 0
    return res

# operation 0 = ADD
# operation 1 = PRODUCT
operations = [0, 1, 2]

@line_profiler.profile
def run():
    solution = 0
    for line in data:
        target = int(line[0])
        values = [int(a) for a in line[1].split(" ")]
        for c in list(itertools.product(operations, repeat=len(values)-1)):
            result = runOperations(values, c, target)
            if result == target:
                solution += result
                break

    print(solution)

run()