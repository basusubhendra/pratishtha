#!/usr/bin/python3
f=open("./zeros6","r")
g=open("./raw_zeros.py","w")
g.write("zeros=[")
lines = f.readlines()
for line in lines:
    l = line.lstrip().rstrip()
    idx = l.index(".")
    l = l[:idx]
    if line != lines[-1]:
       g.write(str(l) + ",")
    else:
       g.write(str(l) + "]")
g.close()
f.close()

