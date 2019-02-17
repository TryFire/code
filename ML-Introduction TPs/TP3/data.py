import sys
import numpy as np

from collections import Counter


def loadTextDataBinary(filename, fixedDictionary=None):
    wfreq = Counter()

    dataset = []
    for line in open(filename, 'r'):
        line = line.split()
        if len(line) <= 1:
            continue
        
        y = int(line[0])
        x = {w: 1 for w in line[1:]}

        if fixedDictionary is None:
            wfreq.update(x.keys())

        dataset.append((x, y))

    if fixedDictionary is None:
        wid = {}
        widr = []
        maxId = 1
        for w, c in wfreq.items():
            if c >= 20 and c < 0.7 * len(dataset):
                wid[w] = maxId
                widr.append(w)
                maxId += 1
    else:
        wid = {w: n + 1 for n, w in enumerate(fixedDictionary)}
        widr = fixedDictionary
        maxId = len(fixedDictionary) + 1
                
    N = len(dataset)

    Xall = np.zeros((N,maxId-1), dtype=float)
    Yall = np.zeros((N,), dtype=float)
    for n in range(len(dataset)):
        x, y = dataset[n]
        Yall[n] = y
        for w in x.keys():
            if w in wid:
                Xall[n,wid[w]-1] = 1.

    return Xall, Yall, widr


def showTree(dt, dictionary):
    left   = dt.tree_.children_left
    right  = dt.tree_.children_right
    thresh = dt.tree_.threshold
    feats  = [ dictionary[i] for i in dt.tree_.feature ]
    value  = dt.tree_.value
    def showTree_(node, s, depth):
        for i in range(depth-1):
            sys.stdout.write('|    ')
        if depth > 0:
            sys.stdout.write('-')
            sys.stdout.write(s)
            sys.stdout.write('-> ')
        if thresh[node] == -2: # leaf
            print('class {}\t({} for class 0, {} for class 1)'.format(np.argmax(value[node]), value[node][0,0], value[node][0,1]))
        else: # internal node
            print('{}?'.format(feats[node]))
            showTree_(left[ node], 'N', depth+1)
            showTree_(right[node], 'Y', depth+1)

    showTree_(0, '', 0)