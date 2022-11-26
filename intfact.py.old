#!/usr/bin/python3

import sys
from mpmath import zetazero
from mpmath import mp
from zeros import zeros
from pi import pi
from e import e
from threading import Thread
from queue import Queue

def get_zero(ctr):
    zero = str(zetazero(ctr).imag)
    idx = zero.index(".")
    zero = zero[idx-1:idx + 9]
    zero = zero.replace(".","0")
    return zero

def further_characterize(net_hits):
    pp = pi[:net_hits]
    ee = e[:net_hits]
    _ee_ = e[:net_hits][::-1]
    mp.prec=28
    mp.dps=28
    states = "" 
    index = 1
    for x in list(zip(pp, ee, _ee_)):
        if x[1] == x[2]:
            states = states + str(get_zero(index))
        index = index + 1
    states = states + "."
    return states

def characterize(rnum):
    l = len(rnum)
    f=open("./stripped_zeros.dat","r")
    lines = f.readlines()
    line_number = -1
    count = 0
    ptr = 0
    states = [] 
    nhits = 0
    net_hits = 0
    niter = 2
    while True:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if int(_tuple_) in zeros:
            net_hits = net_hits + 1
        elif _tuple_ == "00":
            net_hits = net_hits + 1
            if net_hits in zeros:
                state_description = further_characterize(net_hits)
                states.append(state_description)
                nhits = nhits + 1
                if nhits == niter*l:
                    break
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return states

def _count_(x, y):
    pp = ""
    t = 0
    if y == 0:
        pp = pi
    else:
        pp = e
    ctr = 0
    ctr2 = 0
    l = len(x)
    count = 0
    while ctr2 < l:
        ss = x[ctr2]
        _pk_ = pp[ctr]
        if _pk_ == ss and ss == "0":
            _ctr_ = ctr + 1
            _ctr2_ = ctr2 + 1
            _snippet_ = "1"
            while _ctr2_ < l and pp[_ctr_] == x[_ctr2_] and pp[_ctr_] == "0":
                _snippet_ = _snippet_ + "1"
                _ctr_ = _ctr_ + 1
                _ctr2_ = _ctr2_ + 1
            count = count + int(_snippet_, 2)
            ctr2 = _ctr2_
            ctr = 0
            t = 1 - t
            if t == 0 and y == 0:
                pp = pi
            elif t == 0 and y == 1:
                pp = e
            elif t == 1 and y == 0:
                pp = e
            elif t == 1 and y == 1:
                pp = pi
        else:
            ctr = ctr + 1
            ctr2 = ctr2 + 1
    _snippet_ = str(bin(count)[2:])
    return _snippet_

def factorize(states, p, q):
    factor = ""
    t = 0
    for state in states:
        l = len(state)
        factor_snippet = _count_(state, p)
        if t == 0 and p == 1:
           print(p, factor_snippet)
        elif t == 1 and p == 1:
           print(p, factor_snippet[::-1])
        elif p == 0:
           print(p, factor_snippet)
        factor = factor + factor_snippet
        t = 1 - t
    q.put(int(factor,2))
    return

if __name__ == "__main__":
    num = str(sys.argv[1])
    q = Queue()
    states = characterize(num)
    p1 = Thread(target = factorize, args = (states, 0, q, ))
    p2 = Thread(target = factorize, args = (states, 1, q, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    while not q.empty():
       f = q.get()
       print(f)
