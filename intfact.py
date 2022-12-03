#!/usr/bin/python3
import sys
import mpmath

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

if __name__ == "__main__":
    num = str(sys.argv[1])
    precision = int(sys.argv[2])
    triplets = characterize(num, precision)
    print(triplets)

