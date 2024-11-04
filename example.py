import sys
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Parsing folders

samplesUsed = ["atax","simpleconvolution","nw","relu","bicg","spmv","bfs","fft","im2col","concurrentkernel","matrixtranspose","nbody","memcopy","stencil2d","conv2d","fir","kmeans","aes","bitonicsort","matrixmultiplication","floydwarshall","pagerank","fastwalshtransform","concurrentworkload"]
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

for directory, samples in metrics.items():
    for sample in samples:
        dict_metrics = metrics.get(directory)
        aux = dict_metrics.get(sample)
        for i, j in aux.iterrows():
            if j[' what'] == ' kernel_time' and j[' where'] == ' Driver':
                kernels_time[directory][sample] = float(j[' value'])

# No funciona bien
data_serie_kernel = pd.DataFrame(kernels_time)
# data_frame_default = pd.DataFrame(kernels_time.get("default"))
# data_frame_TLB_noMisses = pd.DataFrame(kernels_time.get("TLB_noMisses"))
print(data_serie_kernel)

# sns.barplot(data = data_serie_kernel, 
#              # x='default', y='TLB_noMisses'
#             )
fig, ax = plt.subplots(constrained_layout=True)

key_list = data_serie_kernel.columns.to_list()
xticklabels = data_serie_kernel.index.to_list()

cat_spacing = 0.1
bar_width = (1 - cat_spacing) / len(key_list)

index = np.arange(len(xticklabels))

# Plot bars
for i, key in enumerate(key_list):
    value = data_serie_kernel[key]
    ax.bar(index + i * bar_width, value, width=bar_width, label=key)

ax.set_ylim(0, 0.000000004500)
ax.set_xticks(index + bar_width / 2 * (len(key_list) - 1))
ax.set_xticklabels(xticklabels)
ax.set_xlabel('Samples')
ax.set_ylabel('Kernel Time')
ax.legend(title='Directories')

plt.savefig("example.pdf")
#plt.show()