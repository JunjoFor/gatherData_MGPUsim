import sys

base_directory = "/gpfs/projects/bsc18/bsc125019/mgpusim/samples/"

benchmarks = ["conv2d", "matrixmultiplication", "im2col", "bfs", "spmv", "kmeans", "nbody", "nw"]

for sample in benchmarks:
    # ParseTouches funcionality
    TLB_acceses = 0
    TLB_hit = 0
    TLB_miss = 0
    f = open( base_directory + sample + "/" + sys.argv[1] + "/mem.trace", "r")
    for line in f:
        if "TLB" in line and "hit" in line:
            TLB_acceses += 1
            TLB_hit += 1
        elif "TLB" in line and "miss" in line:
            TLB_acceses += 1
            TLB_miss += 1
    f.close()
    print("Sample: " + sample)
    print("\n TLB miss rate: " + str(TLB_miss/TLB_acceses))