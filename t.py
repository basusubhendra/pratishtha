#!/usr/bin/python3
import sys
f=open("./zeros6","r")
g=open("./zeros_parts.py","w")
lines = f.readlines()
g.write("parts=")
parts = []
for i in range(0, 10):
    part = []
    f.seek(0)
    for j in range(0, 10):
        print([i, j])
        ptr = 0
        ctr = 0
        count = 0
        while count < 10:
            zero = str(lines[ptr]).lstrip().rstrip()
            idx = zero.index(".")
            mantissa = zero[:idx]
            mantissa = mantissa[-2:]
            if mantissa == str(i) + str(j):
                zero_frac = zero[idx + 1:]
                _part_ = zero_frac[(ctr % 4)*2:(ctr % 4)*2 + 2]
                zero_minus_1 = ""
                _part_2 = ""
                if ptr > 0:
                    zero_minus_1 = str(lines[ptr-1]).lstrip().rstrip()
                    idx = zero_minus_1.index(".")
                    zero_frac = zero_minus_1[idx + 1:]
                    _part_2_ = zero_frac[(ctr % 4)*2:(ctr % 4)*2 + 2]
                zero_plus_1 = str(lines[ptr + 1]).lstrip().rstrip()
                idx = zero_plus_1.index(".")
                zero_frac = zero_plus_1[idx + 1:]
                _part_1_ = zero_frac[(ctr % 4)*2:(ctr % 4)*2 + 2]
                part.append([_part_1_, _part_, _part_2_])
                ctr = ctr + 1
                count = count + 1
            ptr = ptr + 1
        parts.append(part)
g.write(str(parts))
g.close()
