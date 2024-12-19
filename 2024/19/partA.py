import functools

lines = [l.replace("\n","") for l in open("myinput").readlines()]

towels = [t.strip() for t in lines[0].split(", ")]
targets = lines[2:]

oTowels = {}
for t in towels:
    if not t[0] in oTowels:
        oTowels[t[0]] = []
    oTowels[t[0]].append(t)


founds = []
@functools.cache
def test(comb, pre = ""):
    global founds
    if comb == "":
        founds.append(pre)
        return True
    print(f"Test {comb} -> {pre}")

    if not comb[0] in oTowels:
        return False
    
    found = False
    for t in oTowels[comb[0]]:
        if len(comb) >= len(t) and comb[:len(t)] == t:
            f = test(comb[len(t):], pre + t)
            if f:
                found = f
                break
    return found


solutions = 0
for t in targets:
    founds = []
    test(t)
    if len(founds) > 0:
        solutions += 1
    print(".")

print(solutions)