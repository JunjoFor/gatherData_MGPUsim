import sys
import os

sample_path = "/gpfs/projects/bsc18/bsc125019/mgpusim/samples/"
samples_paths = ["conv2d", "matrixmultiplication", "im2col", "bfs", "spmv", "kmeans", "nbody", "atax", "nw"]


for sample in samples_paths:
    os.system( "cd " + sample_path + "; module purge ; module load spack ; source /gpfs/projects/bsc18/bsc125019/spack/share/spack/setup-env.sh ; spack load golang ; " + "cd ./" + sample + "; go build ;  mkdir " + sys.argv[1] + "; mv " + sample + " " + sys.argv[1] + "; cp run.sh " + sys.argv[1] + "; cd " + sys.argv[1] + " ; sbatch -A bsc18 -q gp_bsccs run.sh")
