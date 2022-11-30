#!/usr/bin/python3
import sys
def characterize(num):
    triplets = []
    ctr = 0
    l = len(num)
    while True:
        triplet = ""
        for i in range(0, 3):
            triplet = triplet + num[(ctr + i) % l]
        triplets.append(triplet)
        if (ctr + 3) == l:
            break
        ctr = ctr + 1
    return triplets

