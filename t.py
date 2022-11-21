#!/usr/bin/python3
import sys
from mpmath import *
mp.prec=64
mp.dps=64
g=open("./zeros_parts.py","w")

def get_zeros(nn):
    ctr = 1
    ptr = 0
    parts = []
    count = 0
    while count < 11:
        zero = str(zetazero(ctr).imag)
        idx = zero.index(".")
        mantissa = zero[:idx]
        mantissa = mantissa[-2:]
        if mantissa == nn:
            zero = zero[idx + 1:]
            zero = zero[:8]
            part = zero[(ptr % 4)*2:(ptr % 4)*2 + 2]
            ptr = (ptr + 1) 
            parts.append(part)
            count = count + 1
        ctr = ctr + 1
    return parts

g.write("parts=[")
for i in range(0, 10):
    zeros = []
    for j in range(0, 10):
        next_match = str(i) + str(j)
        print(i,j)
        zeros.append(get_zeros(next_match))
    g.write(str(zeros))
g.write("]")
g.close()
