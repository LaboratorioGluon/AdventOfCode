import functools

lines = [l.replace("\n","") for l in open("myinput").readlines()]

towels = [t.strip() for t in lines[0].split(", ")]
targets = lines[2:]

oTowels = {}
for t in towels:
    if not t[0] in oTowels:
        oTowels[t[0]] = []
    oTowels[t[0]].append(t)


cache = {}
def test(comb, pre = ""):
    global founds
    if comb == "":
        return 1

    if not comb[0] in oTowels:
        return False
    
    found = 0
    for t in oTowels[comb[0]]:
        if len(comb) >= len(t) and comb[:len(t)] == t:
            if comb[len(t):] in cache:
                f = cache[comb[len(t):]]
            else:
                f = test(comb[len(t):], pre + t)
            cache[comb[len(t):]] = f
            found += f
            
    return found


solutions = 0
for t in targets:
    founds = []
    ff = test(t)
    #print(f"Founds: {ff}")
    solutions += ff
    #print(".")

print(solutions)