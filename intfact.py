#!/usr/bin/python3

import sys
from decimal import Decimal
from math import modf
from math import ceil
from zeros import zeros

def characterize(rnum):
    l = len(rnum)
    f=open("./stripped_zeros.dat","r")
    lines = f.readlines()
    line_number = -1
    count = 0
    ptr = 0
    nhits = 0
    previous_line_number = 0
    _nzeros_ = 0
    _nprimes_ = 0
    __nzeros__ = 0
    last_state = ""
    state = 0
    states = []
    while nhits < l:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if int(_tuple_) in zeros:
            __nzeros__ = __nzeros__ + 1
            state_description = float(str(modf(Decimal(__nzeros__ / 8.0))[0]))
            if state == 1:
                states.append([last_state, state_description])
                state = 0
                nhits = nhits + 1
            last_state = state_description
        elif _tuple_ == "00":
            state = 1
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return states

if __name__ == "__main__":
    num = str(sys.argv[1])
    pivots = characterize(num[::-1])
    print(pivots)
