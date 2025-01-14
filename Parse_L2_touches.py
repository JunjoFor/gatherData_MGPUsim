import sys
import os

f = open(sys.argv[1] + "/TLBL2_transactions.txt", "r")
outF = open(sys.argv[1] + "page_touches_L2.txt" , "w")

for line in f:
    if "No_touches" in line:
        outF.write(line)
outF.close()
f.close()