#!/usr/bin/python3

import sys
from decimal import Decimal
from math import modf
from zeros_parts import parts

def characterize(num):
    l = len(num)
    ctr = 0
    zeros = []
    offsets = []
    while True:
        triplet = ""
        for i in range(0, 3):
             triplet = triplet + num[(ctr + i) % l]
        mid_element = int(triplet[1])
        if mid_element == 0:
            mid_element = 10
        next_pair = triplet[0] + triplet[2]
        zeros.append(parts[int(triplet[0])][int(triplet[2])][:mid_element])
        ctr = ctr + 1
        delta = ((l - 1) - (ctr + 1)) % 4
        npairs = delta/2.0
        dec = modf(Decimal(npairs))[0]
        if dec > 0:
            if mid_element - int(npairs) == 0:
                npairs = [0,9]
            else:
                npairs = [mid_element-int(npairs), mid_element-(int(npairs) + 1)]
        else:
            npairs = [mid_element-int(npairs)]
        offsets.append(npairs)
        if ctr + 1 == l - 1:
            break
    return zeros,offsets

if __name__ == "__main__":
    num = str(sys.argv[1])
    zeros, offsets = characterize(num)
    print(list(zip(zeros, offsets)))
