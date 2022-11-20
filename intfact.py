#!/usr/bin/python3

import sys
from threading import *
from queue import *
from decimal import *
from math import *
from mpmath import *
from zeros import zeros
num = ""

def characterize(num):
    l = len(num)
    ctr = 0
    triplets = []
    while True:
        triplet = ""
        for i in range(0, 3):
            triplet = triplet + num[(ctr + i) % l]
        triplets.append(triplet)
        ctr = ctr + 1
        if ctr + 3 > l:
            break
    return triplets

def match(t1, t2):
    if t1[0] == t2[0] and t1[2] == t2[2]:
        return True
    else:
        return False

def get_zero(idx):
    mp.prec=64
    mp.dps=64
    zero = str(zetazero(idx).imag)
    i = zero.index(".")
    zero = zero[i - 2:]
    i = zero.index(".")
    zero = zero[i + 1:]
    zero = zero[:16]
    return zero

def get_multiplier(d):
    deficiency = 8 / int(d)
    return deficiency

def factorize(fp, param, q):
    global num
    f=open(fp,"r")
    l = len(num)
    triplets = characterize(num)
    ctr = 0
    while True:
        pos = f.tell()
        triplet = str(f.read(3))
        _triplet_ = triplets[ctr % len(triplets)]
        if match(triplet, _triplet_) == True:
            idx1 = int(_triplet_[1])
            idx2 = int(triplet[1])
            if (pos + idx2)  % 8 == 0:
                ctr = ctr + 1
                zero = get_zero((pos+idx2) / 8)
                dec = Decimal(modf((idx1 - idx2) / 8)[0]).as_integer_ratio()
                denominator = int(dec[1])
                multiplier = get_multiplier(denominator)
                numerator = multiplier*int(dec[0])
                if idx1 < idx2:
                    numerator = 8 + numerator
                else:
                    numerator = 7 + numerator
                q.put([int(zero[int(numerator)]),fp])
                print(list(q.queue))
                input("")
        f.seek(pos+1)
    f.close()

if __name__ == "__main__":
    num = str(sys.argv[1])
    q1 = Queue()
    q2 = Queue()
    t1 = Thread(target=factorize, args = ("pi.txt", 0, q1, ))
    t2 = Thread(target=factorize, args = ("e.txt", 1, q2,  ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
