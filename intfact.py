#!/usr/bin/python3

import sys
from gmpy2 import *
from zeros import zeros
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
    for zz in list(zip(x, y)):
        if zz[0] == zz[1]:
            success = True
            matches.append(zz[0])
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
    while True:
        zero_index = zero_index + increment
        if zero_index <= 0:
            break
        zero = zeros2[zero_index-1]
        matching_digits, success = _match_(zero[1], pivot)
        if success:
            break
        if zero_index == next_zero_index:
            zero_index = next_zero_index
            pivot = zero[1]
            index = index + increment
            if abs(index) < (l - 1):
                next_zero_index = state[index][0]
            else:
                break
    q.put(matching_digits)
    return

def interpret(state):
    q = Queue()
    t1 = Thread(target=traverse_zeros, args = (state, 1, q,  ))
    t2 = Thread(target=traverse_zeros, args = (state, -1, q,  ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    contents = []
    while not q.empty():
        contents.append(q.get())
    if len(contents[0]) == len(contents[1]) and len(contents[0]) == 1 and contents[0] == '0':
        print(contents[0])
        print(contents[1])
        input("Enter any key to continue...")
    elif len(contents[0]) > 1:
        prev_val = contents[0][0]
        for x in contents[0][1:]:
            if prev_val == x and prev_val == '0':
                print(contents[0])
                print(contents[1])
                input("Enter any key to continue...")
            prev_val = x
    elif len(contents[1]) > 1:
        prev_val = contents[1][0]
        for x in contents[1][1:]:
            if prev_val == x and prev_val == '0':
                print(contents[0])
                print(contents[1])
                input("Enter any key to continue...")
            prev_val = x
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
        if int(_tuple_) in zeros:
            net_hits = net_hits + 1
        elif _tuple_ == "00":
            if net_hits in zeros:
                state_description = characterize(net_hits)
                factor = interpret(state_description)
               # if prod(factor1, factor2) == gmpy2.mpz(num):
                #    break
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return states

if __name__ == "__main__":
    num = str(sys.argv[1])
    factors = factorize(num)
