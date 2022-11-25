#!/usr/bin/python3

import sys
from decimal import Decimal
from math import modf
from math import ceil
from zeros100 import zeros100
from primes100 import primes100
from zeros import zeros

state_encoding = [ 0, 1, 1, 0 ]

def further_characterize(net_hits):

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
    net_hits = 0
    while nhits < limit:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if int(_tuple_) in zeros:
            net_hits = net_hits + 1
            __nzeros__ = __nzeros__ + 1
            state_description = str(modf(Decimal(__nzeros__ / 8.0))[0])
            states.append(encode(state_description))
        elif _tuple_ == "00":
            net_hits = net_hits + 1
            if net_hits in zeros:
                z_contrib, p_contrib = further_characterize(net_hits)
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
