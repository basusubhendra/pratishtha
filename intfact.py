#!/usr/bin/python3
import sys
import mpmath
import gmpy2
from linetimer import CodeTimer

def Usage():
    print("Usage:\n./intfact.py <number to be factorized in decimal> <precision in number of digits>\n")
    return 

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
            triplets.append([triplet[1],"00.0"])
        else:
            log_score = str(mpmath.log(score))
            index = log_score.index(".")
            log_score = log_score[index + 1:]
            triplets.append([triplet[1],log_score])
        ctr = ctr + 1
        if (ctr + 3) > l:
            break
    return triplets

def mutual_exclusion(pp, ee):
    excl_set = []
    for x in pp:
        if not x in ee:
            excl_set.append(x)
    return excl_set

def _mask_(pivot, mask, residue_set):
    if not pivot in residue_set:
        residue_set.append(pivot)
    residue_set = sorted(residue_set)
    mask = sorted(mask)
    while True:
        succ = False
        ctr = 0
        for x in residue_set:
            if x in mask:
                del residue_set[ctr]
                succ = True
                break
            ctr = ctr + 1
        if succ == False:
            break
    return residue_set

def factorize(triplets, num):
    fp = open("./pi.txt","r")
    fe = open("./e.txt","r")
    fp.seek(2)
    fe.seek(2)
    ctr = 0
    l = len(triplets)
    residue_set = []
    while True:
        fast_counter = 0
        while  fast_counter < l:
            pp = str(fp.read(5))
            fp_pos = fp.tell()
            ee = str(fe.read(5))
            fe_pos = fe.tell()
            fp.seek(fp_pos-2)
            fe.seek(fe_pos-2)
            triplet = triplets[fast_counter]
            pivot = triplet[0]
            if ctr*3 + 5 > len(triplet[1]):
                print("Out of range error, please increase the range and try.")
                sys.exit(2)
            if triplet[1] != "00.0":
                mask = triplet[1][ctr*3:ctr*3+5]
                residue_set = _mask_(pivot, mask, residue_set)
            nary_set = mutual_exclusion(pp, ee)
            input([nary_set, residue_set])
            fast_counter = fast_counter + 1
        ctr = ctr + 1
    fp.close()
    fe.close()
    return 

if __name__ == "__main__":
    if len(sys.argv) < 3:
        Usage()
        sys.exit(2)
    num = str(sys.argv[1])
    precision = int(sys.argv[2])
    with CodeTimer('Intfact'):
        with CodeTimer('Characterize'):
            triplets = characterize(num, precision)
        print("Stage 1. Characterization Complete.")
        print("Stage 2. Beginning of Factorization.")
        with CodeTimer('Factorize'):
            factorize(triplets, num)
