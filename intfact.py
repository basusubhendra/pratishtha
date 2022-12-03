#!/usr/bin/python3
import sys
import mpmath
import gmpy2

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

def _mask0_(pivot, pp, ee):
    pass

def _mask1_(pivot, mask):
    pass

def factorize(triplets, num):
    fp = open("./pi.txt","r")
    fe = open("./e.txt","r")
    ctr = 0
    l = len(triplets)
    residue_set = []
    interval = 0
    lower_factor = ""
    state = 0
    while True:
        fast_counter = 0
        fp_pos = fp.tell()
        pp = str(fp.read(5))
        fe_pos = fe.tell()
        ee = str(fe.read(5))
        fp.seek(fp_pos-2)
        fe.seek(fe_pos-2)
        while  fast_counter < l:
            triplet = triplets[fast_counter]
            pivot = triplet[0]
            if ctr*3 + 5 > len(triplet[1]):
                print("Out of range error, please increase the range and try.")
                sys.exit(2)
            if triplet[1] == "00.0":
                residue_set = _mask0_(pivot, pp, ee)
            else:
                mask = triplet[1][ctr*3:ctr*3+5]
                residue_set = _mask1_(pivot, mask)
            if len(residue_set) == 0 and state == 1:
                break
            elif len(residue_set) == 0 and state == 0:
                lower_factor = lower_factor + str(interval)[::-1]
                interval = 0
                state = 1
            else:
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
    triplets = characterize(num, precision)
    lower_factor, higher_factor = factorize(triplets, num)
    print(num + "\t=\t" + str(lower_factor) + "\tX\t" + str(higher_factor))

