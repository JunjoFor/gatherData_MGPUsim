import sys
import os

sample_path = "/gpfs/projects/bsc18/bsc125019/mgpusim/samples/"
mgpu_args = " -timing -report-all -unified-gpus=1,2,3,4 -use-unified-memory"
samples_paths = os.listdir(sample_path)



for sample in samples_paths:
    if sample != "runner" and sample != ".gitignore" and sample != "atax" and sample != "stencil2d" and sample != "bfs" and sample != "bitonics":
        #sbatch_file = open(sample_path + sample + "/run.sh", 'w')
        #sbatch_file.write("#!/bin/bash\n#SBATCH -n 1\n#SBATCH -c 2\n#SBATCH --ntasks=4\n#SBATCH --job-name=" + sample +"\nexport SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}\n ./" + sample + mgpu_args)
        #sbatch_file.close()
        os.system( "cd " + sample_path + "; module purge ; module load spack ; source /gpfs/projects/bsc18/bsc125019/spack/share/spack/setup-env.sh ; spack load golang ; " + "cd ./" + sample + "; go build ; sbatch -A bsc18 -q gp_bsccs run.sh")
