#!/usr/bin/python3

import sys
import gmpy2
from pi import pi
from e import e
from threading import Thread
from queue import Queue

def _prod_(factors):
    if len(factors) == 0:
        return "0"
    prod = gmpy2.mpz("1")
    for x in factors:
        prod = gmpy2.mul(prod, gmpy2.mpz(str(x)))
    return prod

def _match_(line, pp, param, q):
    succ = 1
    for x in pp:
        if not x in line:
            succ = None
            break
    #input([line, pp, param, succ])
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
    bnum = str(bin(int(rnum))[2:])
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
    nmatches2 = 0
    ctr = 0
    synth_vector = ""
    factors = []
    factor = ""
    offset = 0
    t = 0
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
            #input(c)
            if c[0][1] != None and c[1][1] != None:
                if t == 0:
                    pass
                else:
                    m = nmatches1
                    nmatches1 = nmatches2
                    nmatches2 = m
                #input([nmatches1, nmatches2])
                synth_vector = str(bin(nmatches1)[2:])
                ctr = 0
                factor = factor + str(bin(nmatches2)[2:])
                dec_factor = int(factor[::-1], 2)
                if divisibleBy(rnum, dec_factor) == True:
                    factors.append(dec_factor)
                    factor = ""
                if synth_vector in bnum:
                    index = bnum.index(synth_vector)
                    if index == offset:
                        offset = offset + len(synth_vector)
                        if offset == len(bnum):
                            break
                    else:
                        print(rnum + " is a prime number.")
                        sys.exit(0)
                else:
                    print(rnum + " is a prime number.")
                    sys.exit(0)
                nmatches1 = 0
                nmatches2 = 0
                t = 1 - t
            elif c[0][1] != None:
                nmatches1 = nmatches1 + 1
                ctr = ctr + 3
            elif c[1][1] != None:
                nmatches2 = nmatches2 + 1
                ctr = ctr + 3
            else:
                ctr = ctr + 3
            nz = gmpy2.mpz(num)
            product = _prod_(factors)
            #input([product, nz])
            if product == nz:
                break
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return factors

if __name__ == "__main__":
    num = str(sys.argv[1])
    factors = factorize(num)
