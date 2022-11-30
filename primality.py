#!/usr/bin/python3

import sys
from common import characterize
def is_prime(num):
    triplets = characterize(num)
    print(triplets)

if __name__ == "__main__":
    num = str(sys.argv[1])
    res = is_prime(num)

