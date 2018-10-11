'''

    Different measure functions

'''

import math

def accuracy(predictions, labels):
    total   = 0
    correct = 0
    for p,l in zip(predictions, labels):
        p = int(round(p))
        if p == l: correct += 1
        total += 1
    return float(correct/total)

