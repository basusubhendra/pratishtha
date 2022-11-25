#!/usr/bin/python3

import sys
from mpmath import zetazero
from mpmath import mp
from decimal import Decimal
from math import modf
from math import ceil
from zeros100 import zeros100
from primes100 import primes100
from zeros import zeros
from pi import pi
from e import e

def get_zero(ctr):
    zero = str(zetazero(ctr).imag)
    idx = zero.index(".")
    zero = zero[idx-1:idx + 9]
    return zero

def further_characterize(net_hits, l):
    pp = pi[:net_hits]
    ee = e[:net_hits]
    _ee_ = e[:net_hits][::-1]
    mp.prec=28
    mp.dps=28
    states = []
    index = 1
    for x in list(zip(pp, ee, _ee_)):
        if x[1] == x[2]:
            states.append([get_zero(index), x[0], x[1]])
        index = index + 1
    return states

def characterize(rnum):
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
    while True:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if int(_tuple_) in zeros:
            net_hits = net_hits + 1
            __nzeros__ = __nzeros__ + 1
        elif _tuple_ == "00":
            net_hits = net_hits + 1
            if net_hits in zeros:
                states = further_characterize(net_hits, l)
                states.append("00")
                nhits = nhits + 1
                if nhits == l:
                    break
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return states 

if __name__ == "__main__":
    num = str(sys.argv[1])
    pivots = characterize(num)
    print(pivots)
