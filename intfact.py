#!/usr/bin/python3
import sys

def characterize(num):
    ctr = 0
    l = len(num)
    triplets = []
    while True:
        triplet = ""
        for i in range(0, 3):
            triplet = triplet + num[(ctr + i) % l]
        triplets.append(triplet)
        ctr = ctr + 1
        if (ctr + 3) > l:
            break
    return triplets

if __name__ == "__main__":
    num = str(sys.argv[1])
    triplets = characterize(num)
    print(triplets)
