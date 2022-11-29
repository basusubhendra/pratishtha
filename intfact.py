#!/usr/bin/python3

import sys
import gmpy2
from pi import pi
from e import e
from threading import Thread
from queue import Queue
"""
from mpmath import zetazero
from mpmath import mp

def get_zero(i):
    mp.prec=64
    mp.dps=64
    z=str(zetazero(i).imag)
    idx = z.index(".")
    z = z[idx-1:]
    idx = z.index(".")
    z = z[:idx+9]
    z=z.replace(".","0")
    return z
"""

def get_zero(i):
    f=open("./stripped_zeros.dat","r")
    lines = f.readlines()
    f.close()
    i = i - 1
    return lines[i].lstrip().rstrip()

def factorize(rnum):
    l = len(rnum)
    line_number = 0 
    count = 0
    ptr = 0
    residue_pi = []
    residue_e = []
    while True:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = get_zero(line_number) 
        _tuple_ = _line_[ptr:ptr+2]
        if _tuple_ == "00":
            _pp_ = pi[line_number]
            _ee_ = e[line_number]
            residue_pi.append(int(_pp_))
            residue_e.append(int(_ee_))
            index = 0
            residue_pi = sorted(residue_pi)
            residue_e = sorted(residue_e)
            for x in residue_pi:
                if str(x) in _line_[1:]:
                    del residue_pi[index]
                index = index + 1
            index = 0
            for x in residue_e:
                if str(x) in _line_[1:]:
                    del residue_e[index]
                index = index + 1
            if len(residue_pi) == len(residue_e) and len(residue_pi) == 0:
                input([line_number, residue_pi, residue_e])
            elif len(residue_pi) > 0 and sorted(residue_pi) == sorted(residue_e):
                input([line_number, residue_pi, residue_e])
        ptr = (ptr + 1) % 8
        count = count + 1
    return

if __name__ == "__main__":
    num = str(sys.argv[1])
    factors = factorize(num)
