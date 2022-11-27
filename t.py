#!/usr/bin/python3
f=open("./stripped_zeros.dat","r")
g=open("./stripped_zeros.py","w")
g.write("stripped_zeros=[")
lines = f.readlines()
f.close()
for line in lines:
    l = line.lstrip().rstrip()
    if line == lines[-1]:
        g.write("\"" + str(l) + "\"" + "]")
    else:
        g.write("\"" + str(l) + "\"" + ",")
g.close()
