import sys
import os

f = open(sys.argv[1] + "/mem.trace", "r")
outF = open(sys.argv[1] + "page_touches.txt" , "w")

for line in f:
    if "No_touches" in line:
        outF.write(line)
outF.close()
f.close()