lines = [l.replace("\n","") for l in open("myinput").readlines()]

ip = 0

for l in lines:
    if "Register A:" in l:
        regA = int(l.split("Register A: ")[-1])
    elif "Register B:" in l:
        regB = int(l.split("Register B: ")[-1])
    elif "Register C:" in l:
        regC = int(l.split("Register C: ")[-1])
    elif "Program:" in l:
        program_ = [int(x) for x in l.split("Program: ")[-1].split(",")]

program = list(zip(program_[0::2], program_[1::2]))

def getCombo(combo):
    if combo <= 3:
        return combo
    elif combo == 4:
        return regA
    elif combo == 5:
        return regB
    elif combo == 6:
        return regC
    elif combo == 7:
        print("INVALID COMBO")
        quit(-1)

def adv(param): #combo
    global regA, regB, regC
    regA = int(regA/2**getCombo(param))

def bxl(param): #literal
    global regA, regB, regC
    regB = regB^param

def bst(param):
    global regA, regB, regC
    regB = getCombo(param)%8

def jnz(param):
    global regA, regB, regC, ip
    if regA == 0:
        return False
    else:
        ip = param
        return True

def bxc(param):
    global regA, regB, regC
    regB = regC^regB

toOutput = ""
outList = []
def out(param):
    global regA, regB, regC, toOutput
    toOutput += str(getCombo(param)%8) + ","
    outList.append(getCombo(param)%8)

def bdv(param):
    global regA, regB, regC
    regB = int(regA/2**getCombo(param))

def cdv(param):
    global regA, regB, regC
    regC = int(regA/2**getCombo(param))


funcMap = [
    adv,
    bxl,
    bst,
    jnz,
    bxc,
    out,
    bdv,
    cdv
]

def runProgram(ops):
    global ip
    while ip < len(ops):
        op = ops[ip][0]
        param = ops[ip][1]
        ret = funcMap[op](param)
        if ret == None or ret == False:
            ip += 1
        elif ret == True:
            pass

def printStatus():
    print(f"Regs: {regA}, {regB}, {regC}")


def test(A,B,C):
    global regA, regB, regC, ip, toOutput, outList
    regA = A
    regB = B
    regC = C
    toOutput = ""
    ip = 0
    outList = []
    runProgram(program)
    #print(f"{A:3} -> Out: {toOutput} ", end="")

program_.reverse()
toCheck = [(0, 0)]
solutions = []
while toCheck:
    index, mindex = toCheck.pop()
    for i in range(8):
        test(i+index,0,0)
        if outList[0] == program_[mindex]:
            if mindex+1 >= len(program_):
                solutions.append(i+index)
            else:
                toCheck.append( (8*(index+i), mindex+1) )

print(min(solutions))

