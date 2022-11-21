#!/usr/bin/python3

import sys
from decimal import Decimal
from math import modf
from mpmath import *

def get_fractional_part(ctr):
    mp.prec=64
    mp.dps=64
    zero = str(zetazero(ctr).imag)
    idx = zero.index(".")
    mantissa = zero[:idx]
    mantissa = mantissa[-2:]
    zero = zero[idx+1]
    zero = zero[:8]
    return mantissa, zero

def _get_zero_(next_pair, ctr, ptr % 4:
        mantissa, zero = get_fractional_part(ctr)
        if mantissa == next_pair:
           return True, zero[ptr*2:ptr*2+2]
        else:
           return False, None

def get_zeros(next_pair, mid_element):
    mp.prec=64
    mp.dps=64
    ctr = 1
    ptr = 0
    _set_ = []
    while ptr < mid_element:
        success, zero = _get_zero_(next_pair, ctr, ptr % 4)
        if success:
            ptr = ptr + 1
            success = False
            _set_.append(zero)
        ctr = ctr + 1
    return _set_

def characterize(num):
    l = len(num)
    ctr = 0
    triplets = []
    offsets = []
    while True:
        triplet = ""
        for i in range(0, 3):
             triplet = triplet + num[(ctr + i) % l]
        mid_element = int(triplet[1])
        if mid_element == 0:
            mid_element = 10
        next_pair = triplet[0] + triplet[2]
        triplets.append(get_zeros(next_pair, mid_element))
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
