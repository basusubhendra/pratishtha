#!/usr/bin/python3

import sys
from decimal import Decimal
from math import modf
from mpmath import *

def characterize(num):
    l = len(num)
    ctr = 0
    triplets = []
    offsets = []
    while True:
        triplet = ""
        for i in range(0, 3):
             triplet = triplet + num[(ctr + i) % l]
        triplets.append(triplet)
        ctr = ctr + 1
        delta = (l - 1) - (ctr + 1)
        npairs = delta/2.0
        dec = modf(Decimal(npairs))[0]
        if dec > 0:
            npairs = [int(npairs), int(npairs) + 1]
        else:
            npairs = [int(npairs)]
        offsets.append(npairs)
        if ctr + 1 == l - 1:
            break
    return triplets, offsets

if __name__ == "__main__":
    num = str(sys.argv[1])
    print(num)
    triplets, offsets = characterize(num)
    print(list(zip(triplets, offsets)))
