#!/usr/bin/python3

import sys

def characterize(rnum):
    l = len(rnum)
    f=open("./stripped_zeros.txt","r")
    lines = f.readlines()
    line_number = -1
    count = 0
    ptr = 0
    nhits = 0
    pivots = []
    while nhits < l:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if _tuple_ == "00":
            pivots.append(line_number + 1)
            nhits = nhits + 1
        ptr = (ptr + 1) % 8
        count = count + 1
    return pivots

if __name__ == "__main__":
    num = str(sys.argv[1])
    #reverse is for analysis
    pivots = characterize(num[::-1])
    print(pivots)
