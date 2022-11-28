#!/usr/bin/python3

import sys
from gmpy2 import *
from pi import pi
from e import e
from threading import Thread
from queue import Queue

def prod(factors):
    if len(factors) == 0:
        return "0"
    prod = gmpy2.mpz("1")
    for x in factors:
        prod = gmpy2.mul(prod, gmpy2.mpz(str(x)))
    return str(prod)

def _match_(line, pp, param, q):
    succ = 1
    for x in pp:
        if not x in pp:
            succ = None
            break
    q.put([param, succ])
    return

def divisibleBy(num, factor):
    nz = gmpy2.mpz(num)
    fz = gmpy2.mpz(factor)
    if fz <= gmpy2.mpz("1"):
        return False
    modz = gmpy2.f_mod(nz, fz)
    if modz == gmpy2.mpz("0"):
        return True
    else:
        return False

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
    nmatches1 = 0
    namtches2 = 0
    ctr = 0
    factors = []
    factor = ""
    offset = 0
    while True:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if _tuple_ == "00":
            q = Queue()
            t1 = Thread(target=_match_, args=(_line_, pi[ctr:ctr + 5], 0, q,  ))
            t2 = Thread(target=_match_, args=(_line_, e[ctr:ctr + 5], 1, q,  ))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            c = []
            while not q.empty():
                c.append(q.get())
            input(c)
            if c[0][1] != None and c[1][1] != None:
                ctr = 0
                synth_vector = synth_vector + str(bin(nmatches1)[2:])
                factor = factor + str(bin(nmatches2[::-1])[2:])
                dec_factor = int(factor, 2)
                if divisibleBy(rnum, dec_factor) == True:
                    factors.append(dec_factor)
                    factor = ""
                if synth_vector in str(bin(rnum)[2:])[::-1][offset:]:
                    index = str(bin(rnum)[2:])[::-1][offset:].index(synth_vector)
                    if index == 0:
                        offset = offset + len(synth_vector)
                        if offset == l:
                            break
                else:
                    print(rnum + " is a prime number.")
                    sys.exit(0)
            elif c[0][1] != None:
                nmatches1 = nmatches1 + 1
                ctr = ctr + 3
            elif c[1][1] != None:
                nmatches2 = nmatches2 + 1
                ctr = ctr + 3
            else:
                ctr = ctr + 3
            if prod(factors) == gmpy2.mpz(num):
                break
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return states

if __name__ == "__main__":
    num = str(sys.argv[1])
    factors = factorize(num)
