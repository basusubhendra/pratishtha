#!/usr/bin/python3
import sys
import mpmath
import gmpy2
from linetimer import CodeTimer

def _divide_(num, factor):
    nz = gmpy2.mpz(num)
    fz = gmpy2.mpz(factor)
    if fz == gmpy2.mpz("0"):
        print("Divide by zero exception")
        sys.exit(2)
    qz = gmpy2.f_div(nz, fz)
    return str(qz)

def characterize(num, precision):
    ctr = 0
    l = len(num)
    mpmath.mp.dps = precision
    mpmath.mp.prec = precision
    triplets = []
    while True:
        triplet = ""
        for i in range(0, 3):
            triplet = triplet + num[(ctr + i) % l]
        score = triplet[0] + triplet[2] + "." + triplet[1]
        if score == "00.0":
            triplets.append([triplet[2],"00.0"])
        else:
            log_score = str(mpmath.log(score))
            index = log_score.index(".")
            log_score = log_score[index + 1:]
            triplets.append([triplet[2],log_score])
        ctr = ctr + 1
        if (ctr + 3) > l:
            break
    return triplets

def _mask0_(pivot, pp, ee, residue_set):
    if not pivot in residue_set:
        residue_set.append(pivot)
    ctr = 0
    for x in residue_set:
        if x in pp and not x in ee:
            del residue_set[ctr]
        ctr = ctr + 1
    return residue_set

def _mask1_(pivot, mask, residue_set):
    if not pivot in residue_set:
        residue_set.append(pivot)
    ctr = 0
    for x in residue_set:
        if x in mask:
            del residue_set[ctr]
        ctr = ctr + 1
    return residue_set

def factorize(triplets, num):
    nz = gmpy2.mpz(num)
    fp = open("./pi.txt","r")
    fe = open("./e.txt","r")
    fp.seek(2)
    fe.seek(2)
    ctr = 0
    l = len(triplets)
    residue_set = []
    interval = 0
    lower_factor = ""
    state = 0
    while True:
        fast_counter = 0
        pp = str(fp.read(5))
        fp_pos = fp.tell()
        ee = str(fe.read(5))
        fe_pos = fe.tell()
        fp.seek(fp_pos-2)
        fe.seek(fe_pos-2)
        while  fast_counter < l:
            triplet = triplets[fast_counter]
            pivot = triplet[0]
            if ctr*3 + 5 > len(triplet[1]):
                print("Out of range error, please increase the range and try.")
                sys.exit(2)
            if triplet[1] == "00.0":
                residue_set = _mask0_(pivot, pp, ee, residue_set)
            else:
                mask = triplet[1][ctr*3:ctr*3+5]
                residue_set = _mask1_(pivot, mask, residue_set)
            if len(residue_set) == 0 and state == 1:
                break
            elif len(residue_set) == 0 and state == 0:
                lower_factor = lower_factor + str(interval)[::-1]
                if gmpy2.mpz(lower_factor[::-1]) > nz:
                    print("Something wrong with the core logic.")
                    sys.exit(2)
                interval = 0
                state = 1
            elif len(residue_set) > 0:
                state = 0
                interval = interval + 1
            fast_counter = fast_counter + 1
        ctr = ctr + 1
    lower_factor = lower_factor[::-1]
    higher_factor = _divide_(num, lower_factor)
    fp.close()
    fe.close()
    return lower_factor, higher_factor

if __name__ == "__main__":
    num = str(sys.argv[1])
    precision = int(sys.argv[2])
    with CodeTimer('Intfact'):
        with CodeTimer('Characterize'):
            triplets = characterize(num, precision)
        print("Stage 1. Characterization Complete.")
        print("Stage 2. Beginning of Factorization.")
        with CodeTimer('Factorize'):
            lower_factor, higher_factor = factorize(triplets, num)
            print(num + "\t=\t" + str(lower_factor) + "\tX\t" + str(higher_factor))
