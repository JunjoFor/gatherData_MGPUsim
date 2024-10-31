import sys
import os

sample_path = "/gpfs/projects/bsc18/bsc125019/mgpusim/samples/"
mgpu_args = " -timing -report-all -unified-gpus=1,2,3,4 -use-unified-memory"
samples_paths = os.listdir(sample_path)


for sample in samples_paths:
    if sample != "runner":
        os.system( "cd " + sample_path + "; module purge ; module load spack ; source /gpfs/projects/bsc18/bsc125019/spack/share/spack/setup-env.sh ; spack load golang ; " + "cd ./" + sample + "; go build ; sbatch --job-name=" + sample + " ./" + sample + mgpu_args)
