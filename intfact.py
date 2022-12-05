#!/usr/bin/python3
import sys
import mpmath
import gmpy2
from linetimer import CodeTimer
from pi import pi
from e import e

def Usage():
    print("Usage:\n./intfact.py <number to be factorized in decimal> <precision in number of digits> <number of stages>\n")
    return 

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
            if not x in excl_set:
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

def _exclusive_(s1):
    if len(s1) == 0:
        return True
    ss1 = sorted(list(set(map(int,s1))))
    if (len(ss1) == 1 and (ss1[0] == 0 or ss1[0] == 8)) or (len(ss1) == 2 and ss1 == [0, 8]):
        return True
    else:
        return False
    return False

def find_mutual_exclusions(triplets, num, nstages):
    fp = open("./pi.txt","r")
    fe = open("./e.txt","r")
    fp.seek(2)
    fe.seek(2)
    ctr = 0
    l = len(triplets)
    residue_set = []
    interval = 0
    offset = -1
    stages = []
    counter = 0
    nary_sets = []
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
            if len(residue_set) == 0:
                nary_set1 = mutual_exclusion(pp, ee)
                nary_set2 = mutual_exclusion(ee, pp)
                nary_sets.append([nary_set1, nary_set2])
                if _exclusive_(nary_set1) or _exclusive_(nary_set2):
                    stages.append(nary_sets)
                    nary_sets = []
                    counter = counter + 1
                    if counter == nstages:
                        return stages
            fast_counter = fast_counter + 1
        ctr = ctr + 1
    fp.close()
    fe.close()
    return stages

def factorize(stages):
    factor1 = ""
    factor2 = ""
    parity_left = 1
    parity_right = 1
    factor_snippets = []
    left_pp = ""
    right_pp = ""
    state = 0
    for stage in stages:
        left_index_pp = 0
        right_index_pp = 0
        interval = 0
        if parity_left == 1:
            left_pp = pi
        else:
            left_pp = e
        if parity_right == 1:
            right_pp = pi
        else:
            right_pp = e
        for s in stage:
            lhs = s[0]
            rhs = s[1]
            len_lhs = len(lhs)
            len_rhs = len(rhs)
            _left_index_pp_ = left_index_pp
            for x in lhs:
                if x in left_pp[:len_lhs]:
                    _left_index_pp_ = _left_index_pp_ + 1
            _right_index_pp_ = right_index_pp
            for x in rhs:
                if x in right_pp[:len_rhs]:
                    _right_index_pp_ = _right_index_pp_ + 1
            if _left_index_pp_ > left_index_pp and _right_index_pp_ > right_index_pp:
                if left_parity == right_parity and state == 0:
                    interval = interval + 1
                elif left_parity == right_parity and state == 1:
                    factor_snippets.append(bin(interval)[2:])
                    interval = 0
                    state = 0
                elif left_parity != right_parity and state == 1:
                    interval = interval + 1
                elif left_parity != right_parity and state == 0:
                    factor_snippets.append(bin(interval)[2:])
                    interval = 0
                    state = 1
            if len(lhs) == 0 or _exclusive_(lhs):
                left_parity = 1 - left_parity
            if len(rhs) == 0 or _exclusive_(rhs):
                right_parity = 1 - right_parity
            if (len(lhs) == 0 or _exclusive_(lhs)) and (len(rhs) == 0 or _exclusive_(rhs)):
                break
    input(factor_snippets)
    return factor1, factor2

if __name__ == "__main__":
    if len(sys.argv) < 4:
        Usage()
        sys.exit(2)
    num = str(sys.argv[1])
    precision = int(sys.argv[2])
    nstages = int(sys.argv[3])
    with CodeTimer('Intfact'):
        with CodeTimer('Characterize'):
            triplets = characterize(num, precision)
        print("Stage 1. Characterization Complete.")
        print("Stage 2. Beginning of Factorization.")
        with CodeTimer('Mutexes'):
            stages = find_mutual_exclusions(triplets, num, nstages)
            for s in stages:
                for x in s:
                    print(x)
                input("\n")
        with CodeTimer('Factorize'):
            factor1, factor2 = factorize(stages)
