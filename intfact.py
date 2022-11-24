#!/usr/bin/python3

import sys
from zeros import zeros
from primes import primes

def further_characterize(previous_line_number,line_number):
    f=open("./pi.txt","r")
    g=open("./e.txt","r")
    f.seek(previous_line_number)
    g.seek(previous_line_number)
    pos = previous_line_number
    while pos < line_number:
        c=str(f.read(1))
        d=str(g.read(1))
        probable_zero = int(c + d)
        probable_prime = int(d + c)
        if probable_zero in zeros:
            nzeros = nzeros + 1
        if probable_prime in primes:
            nprimes = nprimes + 1
        pos = pos + 1
    f.close()
    g.close()
    return nzeros, nprimes

    
def characterize(rnum):
    l = len(rnum)
    f=open("./stripped_zeros.txt","r")
    lines = f.readlines()
    line_number = -1
    count = 0
    ptr = 0
    nhits = 0
    zero_pivots = []
    prime_pivots = []
    previous_line_number = 0
    _nzeros_ = 0
    _nprimes_ = 0
    while nhits < l:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if _tuple_ == "00":
            nzeros, nprimes = _further_characterize_(previous_line_number, line_number + 1)
            _nzeros_ = _nzeros_ + nzeros
            _nprimes_ = _nprimes_ + nprimes
            previous_line_number = line_number + 2
            zero_pivots.append(_nzeros_)
            prime_pivots.append(_nprimes_)
            nhits = nhits + 1
        ptr = (ptr + 1) % 8
        count = count + 1
    return zero_pivots, prime_pivots

if __name__ == "__main__":
    num = str(sys.argv[1])
    #reverse is for analysis
    zero_pivots, prime_pivots = characterize(num[::-1])
    print(zero_pivots)
    print(prime_pivots)
