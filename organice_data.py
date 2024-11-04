import sys
import os

sample_path = "/gpfs/projects/bsc18/bsc125019/mgpusim/samples/"
samples_paths = os.listdir(sample_path)

sucessful_samples = open("./good_samples.txt", 'w')

for sample in samples_paths:
    if sample != "runner" and sample != ".gitignore":
        files = os.listdir(sample_path + sample)
        if("metrics.csv" in files):
            print(sample + " Se ejecutó correctamente")
            sucessful_samples.write(sample + ",")
            os.system("cd " + sample_path + sample + " ; mkdir " + sys.argv[1] + "; mv metrics.csv " + sample + " slurm* ./" + sys.argv[1])