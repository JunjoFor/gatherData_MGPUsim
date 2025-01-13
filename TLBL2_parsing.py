import sys

base_directory = "/gpfs/projects/bsc18/bsc125019/mgpusim/samples/"

benchmarks = ["conv2d", "matrixmultiplication", "im2col", "bfs", "spmv", "kmeans", "nbody", "nw"]

for sample in benchmarks:
    # ParseTouches funcionality
    f = open( base_directory + sample + "/" + sys.argv[1] + "/mem.trace", "r")
    outF = open(base_directory + sample + "/" + sys.argv[1] + "/TLBL2_transactions.txt" , "w")

    for line in f:
        if "L2TLB" in line:
            outF.write(line)
    outF.close()
    f.close()