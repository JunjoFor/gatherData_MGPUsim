import sys
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Parsing folders

samplesUsed = ["fir", "bfs"]
secondDir = ["default", "TLB_noMisses"]
metrics = {}
kernels_time = {}

for dir in secondDir:
    for sample in samplesUsed:
        metrics[dir] = {}
        kernels_time[dir] = {}

for dir in secondDir:
    # kernels_time[dir]['Benchmark'] = samplesUsed
    for sample in samplesUsed:
        metrics[dir][sample] = pd.read_csv("../mgpusim/samples/" + sample + "/" + dir + "/metrics.csv")

for single_m, multi_metric in metrics.items():
    for metric in multi_metric:
        dict_metrics = metrics.get(single_m)
        aux = dict_metrics.get(metric)
        for i, j in aux.iterrows():
            if j[' what'] == ' kernel_time':
                kernels_time[single_m][metric] = [j[' value']]

# No funciona bien
data_serie_kernel = pd.DataFrame(kernels_time)
# data_frame_default = pd.DataFrame(kernels_time.get("default"))
# data_frame_TLB_noMisses = pd.DataFrame(kernels_time.get("TLB_noMisses"))
print(data_serie_kernel)

# sns.barplot(data = data_serie_kernel, x='default', y='TLB_noMisses')
