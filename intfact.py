#!/usr/bin/python3

import sys
from decimal import Decimal
from math import modf
from zeros import zeros

def characterize(rnum, limit):
    l = len(rnum)
    f=open("./stripped_zeros.txt","r")
    lines = f.readlines()
    line_number = -1
    count = 0
    ptr = 0
    nhits = 0
    previous_line_number = 0
    _nzeros_ = 0
    _nprimes_ = 0
    pivots = []
    __nzeros__ = 0
    while nhits < limit:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if int(_tuple_) in zeros:
            __nzeros__ = __nzeros__ + 1
            pivots.append(float(str(modf(Decimal(__nzeros__ / 8.0))[0])))
            nhits = nhits + 1
        elif _tuple_ == "00":
            pivots.append("00")
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return pivots

if __name__ == "__main__":
    num = str(sys.argv[1])
    limit = int(sys.argv[2])
    #reverse is for analysis
    pivots = characterize(num[::-1], limit)
    print(pivots)
