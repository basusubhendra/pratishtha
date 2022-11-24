#!/usr/bin/python3
import sys
f=open("./zeros.txt","r")
g=open("./stripped_zeros.txt","w")
lines = f.readlines()
f.close()
for line in lines:
    l = line.rstrip().lstrip()
    idx = l.index(".")
    l = l[idx-1:idx + 9]
    l = l.replace(".","")
    g.write(str(l) + "\n")
g.close()
