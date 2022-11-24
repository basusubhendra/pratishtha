#!/usr/bin/python3

import sys
from decimal import Decimal
from math import modf
from math import ceil
from zeros import zeros

state_encoding = dict([])
state_encoding["0.0"] = "000"
state_encoding["0.125"] = "001"
state_encoding["0.25"] = "010"
state_encoding["0.375"] = "011"
state_encoding["0.5"] = "100"
state_encoding["0.625"] = "101"
state_encoding["0.75"] = "110"
state_encoding["0.875"] = "111"

def encode(ss):
    global state_encoding
    return state_encoding[ss]

def _aggregate_(sd):
    return sd.count("0"), sd.count("1")

def characterize(rnum, limit):
    l = len(rnum)
    f=open("./stripped_zeros.dat","r")
    lines = f.readlines()
    line_number = -1
    count = 0
    ptr = 0
    states = []
    nhits = 0
    __nzeros__ = 0
    while nhits < limit:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if int(_tuple_) in zeros:
            __nzeros__ = __nzeros__ + 1
            state_description = str(modf(Decimal(__nzeros__ / 8.0))[0])
            states.append(encode(state_description))
        elif _tuple_ == "00":
            states.append("**")
            nhits = nhits + 1
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return states

if __name__ == "__main__":
    num = str(sys.argv[1])
    limit = int(sys.argv[2])
    pivots = characterize(num, limit)
    print(pivots)
