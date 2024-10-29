import sys
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# sns.set_theme(style="whitegrid")

# Parsing folders

samplesUsed = ["fir", "bfs"]
secondDir = ["default"]
metrics = {}
kernels_time = {}

for dir in secondDir:
    for sample in samplesUsed:
        metrics[dir] = {}
        kernels_time[dir] = {}

for dir in secondDir:
    for sample in samplesUsed:
        metrics[dir][sample] = pd.read_csv("../mgpusim/samples/" + sample + "/" + dir + "/metrics.csv")
        kernels_time[dir]['Benchmark'] = 'Kenel Time'

for single_m, multi_metric in metrics.items():
    for metric in multi_metric:
        dict_metrics = metrics.get(single_m)
        aux = dict_metrics.get(metric)
        for i, j in aux.iterrows():
            if j[' what'] == ' kernel_time':
                kernels_time[single_m][metric] = j[' value']

data_frame_kernel = {}
for dir in secondDir:
    data_frame_kernel[dir] = pd.Series(kernels_time.get(dir))

for frame in data_frame_kernel:
    print(frame)
    print(data_frame_kernel.get(frame))