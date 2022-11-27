#!/usr/bin/python3

import sys
from gmpy2 import *
from zeros import zeros100
from zeros2 import zeros2
from pi import pi
from e import e
from threading import Thread
from queue import Queue

def characterize(net_hits):
    pp = pi[:net_hits]
    ee = e[:net_hits]
    _ee_ = e[:net_hits][::-1]
    states = [] 
    index = 0
    for x in list(zip(pp, ee, _ee_)):
        if x[1] == x[2]:
            zero = zeros2[index]
            states.append([index + 1, zero[0], zero[1]])
        index = index + 1
    return states

def _match_(x, y):
    matches = []
    success = False
    ctr = 0
    for zz in list(zip(x, y)):
        if zz[0] == zz[1]:
            success = True
            matches.append([ctr, zz[0]])
        ctr = ctr + 1
    return matches, success

def traverse_zeros(state, param, q):
    l = len(state)
    increment = param
    index = 0
    if param == 1:
        index = 0
    elif param == -1:
        index = -1
    zero_index = state[index][0]
    next_zero_index = zero_index 
    if abs(index + increment) < (l - 1):
        next_zero_index = state[index + increment][0]
    else:
        return
    pivot = state[index][2]
    matching_digits = []
    _matches_ = []
    while True:
        zero_index = zero_index + increment
        if zero_index <= 0 or zero_index > state[-1][0]:
            break
        zero = zeros2[zero_index-1]
        matching_digits, success = _match_(zero[1], pivot)
        if success:
            _matches_.append(matching_digits)
        if zero_index == next_zero_index:
            zero_index = next_zero_index
            pivot = zero[1]
            index = index + increment
            if abs(index) < (l - 1):
                next_zero_index = state[index][0]
            else:
                break
    q.put(_matches_)
    return

def interpret(state):
    q = Queue()
    t1 = Thread(target=traverse_zeros, args = (state, 1, q,  ))
    t2 = Thread(target=traverse_zeros, args = (state, -1, q,  ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    while not q.empty():
        print(q.get())
        print("%%%%%%%")
    input("<=======================>")
    return None

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
        if int(_tuple_) in zeros100:
            net_hits = net_hits + 1
        elif _tuple_ == "00":
            state_description = characterize(net_hits)
            factor = interpret(state_description)
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
