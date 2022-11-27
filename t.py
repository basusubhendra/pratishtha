#!/usr/bin/python3
from zeros2 import zeros2
f=open("./_zeros2.py","w")
f.write("zeros2=[")
for zero in zeros2:
    zeros = zero.split(".")
    f.write("[")
    f.write("\"")
    f.write(zeros[0])
    f.write("\"")
    f.write(",")
    f.write("\"")
    f.write(zeros[1][:-1])
    f.write("\"")
    f.write("]")
    f.write(",")
f.write("]")
f.close()
