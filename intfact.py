#!/usr/bin/python3

import sys
from mpmath import zetazero
from mpmath import mp
from gmpy2 import *
from zeros import zeros
from pi import pi
from e import e

def get_zero(ctr):
    zero = str(zetazero(ctr).imag)
    idx = zero.index(".")
    frac = zero[idx:idx + 9]
    mantissa = zero[:idx]
    return mantissa, frac[1:]

def characterize(net_hits):
    pp = pi[:net_hits]
    ee = e[:net_hits]
    _ee_ = e[:net_hits][::-1]
    mp.prec=28
    mp.dps=28
    states = [] 
    index = 1
    for x in list(zip(pp, ee, _ee_)):
        if x[1] == x[2]:
            mantissa, frac = get_zero(index)
            states.append([index, int(mantissa), frac])
        index = index + 1
    return states

def interpret(state, t):
    pass

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
    t = 0
    while True:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if int(_tuple_) in zeros:
            net_hits = net_hits + 1
        elif _tuple_ == "00":
            if net_hits in zeros:
                state_description = characterize(net_hits)
                input(state_description)
                factor = interpret(state_description, t)
                if t == 0:
                    factor1.append(factor)
                elif t == 8:
                    factor2.append(factor)
                t = 8 - t
               # if prod(factor1, factor2) == gmpy2.mpz(num):
                #    break
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return states

if __name__ == "__main__":
    num = str(sys.argv[1])
    factors = factorize(num)
    print(factors)
