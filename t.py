#!/usr/bin/python3
import sys
f=open("./zeros6","r")
g=open("./zeros.py","w")
lines = f.readlines()
g.write("zeros=[")
for line in lines:
    l = line.rstrip().lstrip()
    idx = l.index(".")
    l = l[:idx]
    l = l[-2:]
    if line == lines[-1]:
        g.write("\"" + str(l) + "\"" )
    else:
        g.write("\"" + str(l) + "\"" + ",")
g.write("]")
g.close()
