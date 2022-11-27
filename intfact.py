#!/usr/bin/python3

import sys
from gmpy2 import *
from zeros2 import zeros2

def prod(f1, f2):
    _prod_ = gmpy2.mul(gmpy2.mpz(f1), gmpy2.mpz(f2))
    return str(_prod_)

def factorize(rnum):
    l = len(rnum)
    f=open("./stripped_zeros.dat","r")
    lines = f.readlines()
    line_number = -1
    count = 0
    ptr = 0
    net_hits = 0
    prod = gmpy2.mpz("1")
    factor1 = []
    factor2 = []
    while True:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if _tuple_ == "00":
            state_description = zeros2[line_number][1]
            input([ptr,state_description])
            print("!!==================!!")
            #if prod(factor1, factor2) == gmpy2.mpz(num):
            #    break
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return states

if __name__ == "__main__":
    num = str(sys.argv[1])
    factors = factorize(num)
