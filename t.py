#!/usr/bin/python3
import sys
f=open("./zeros6","r")
g=open("./zeros_parts.py","w")
lines = f.readlines()
f.close()
g.write("parts=")
part = []
for i in range(0, 10):
    _parts_ = []
    for j in range(0, 10):
        print([i, j])
        next_match = str(i) + str(j)
        ptr = 0
        ctr = 0
        count = 0
        _part2_ = []
        while count < 10:
            zero = str(lines[ptr]).lstrip().rstrip()
            idx = zero.index(".")
            mantissa = zero[:idx]
            mantissa = mantissa[-2:]
            if mantissa == next_match:
                idx = zero.index(".")
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
                _part2_.append([_part_2_, _part_, _part_1_])
                #input([zero[:idx], _part_2_, _part_, _part_1_])
                ctr = ctr + 1
                count = count + 1
            ptr = ptr + 1
        _parts_.append(_part2_)
    part.append(_parts_)
g.write(str(part))
g.close()
