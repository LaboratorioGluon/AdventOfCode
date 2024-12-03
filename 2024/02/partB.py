import numpy as np

DEBUG = False

data = [ [int(s) for s in l.replace("\n","").split()] for l in open("myinput","r").readlines()] 
#data = [ [int(s) for s in l.replace("\n","").split()] for l in open("test","r").readlines()] 


def valid(d, second = False):
    return (max(np.abs(np.diff(d))) <= 3) and (min(np.abs(np.diff(d))) >= 1) and ((np.sum(np.diff(d) > 0) == len(d)-1) or (np.sum(np.diff(d) < 0) == len(d)-1))


valids = []
for d in data:
    if not valid(d):
        for i in range(len(d)):
            newd = list(d)
            newd.pop(i)
            newvalid = valid(newd)
            if newvalid == True:
                valids.append(1)
                break
    else:
        valids.append(1)


print(np.sum(valids))