import numpy as np

DEBUG = False

data = [ [int(s) for s in l.replace("\n","").split()] for l in open("myinput","r").readlines()] 
#data = [ [int(s) for s in l.replace("\n","").split()] for l in open("test","r").readlines()] 


def valid(d):
    if DEBUG:
        print(f"Test {d}")
        print(np.diff(d))
        print(abs(max(np.diff(d))) <= 3)
        print(abs(min(np.diff(d))) >= 1)
        print(f"{(np.sum(np.diff(d) > 0) == len(d)-1)} || {(np.sum(np.diff(d) < 0) == len(d)-1)}")
    return (max(np.abs(np.diff(d))) <= 3) and (min(np.abs(np.diff(d))) >= 1) and ((np.sum(np.diff(d) > 0) == len(d)-1) or (np.sum(np.diff(d) < 0) == len(d)-1))


valids = [valid(d) for d in data]

print(np.sum(valids))