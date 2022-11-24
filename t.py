#!/usr/bin/python3
import sys
f=open("./zeros6","r")
g=open("./stripped_zeros.txt","w")
lines = f.readlines()
f.close()
for line in lines:
    l = str(line).lstrip().rstrip()
    idx = l.index(".")
    l = l[idx-1:]
    idx = l.index(".")
    l = l[idx-1:10]
    l = l.replace(".","")
    g.write(str(l)  + "\n")
g.close()
f.close()
