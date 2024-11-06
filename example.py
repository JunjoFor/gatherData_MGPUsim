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

kernels_time["TLB_misses"] = {}
kernels_time["Instructions"] = {}

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
        tlb_misses = 0.0
        insts = 0.0
        for i, j in aux.iterrows():
            if j[' what'] == ' kernel_time' and j[' where'] == ' Driver':
                kernels_time[directory][sample] = float(j[' value'])
            if directory == "default" and j[' what'] == ' cu_inst_count':
                insts = insts + float(j[' value'])
            component = j[' where'].split(".")
            if len(component) > 3:
                if directory =="default" and component[3] == "L1VTLB[0]" and j[' what'] == 'miss':
                    tlb_misses = tlb_misses + float(j[' value'])
            kernels_time["Instructions"][sample] = insts
            kernels_time["TLB_misses"][sample] = tlb_misses

# No funciona bien
data_serie_kernel = pd.DataFrame(kernels_time)

data_ipc = pd.DataFrame()
default_value = 0.0
tlbNoMisses_value = 0.0
for row in data_serie_kernel.itertuples(index=True):
    if row.default <= 0:
        data_ipc.loc[row[0], 'default'] = 0
    else:
        data_ipc.loc[row[0], 'default'] = row.default / row.default
    if row.TLB_noMisses <= 0:
        data_ipc.loc[row[0], 'TLB_noMisses'] = 0
    else:
        data_ipc.loc[row[0], 'TLB_noMisses'] = row.default / row.TLB_noMisses
    if row.Instructions <= 0:
        data_ipc.loc[row[0], "MPKI"] = 0.0
    else:
        data_ipc.loc[row[0], "MPKI"] = row.TLB_misses / (row.Instructions/1000.0)
    
sorted_df = data_ipc.sort_values(by="MPKI", ascending=False)

# data_frame_default = pd.DataFrame(kernels_time.get("default"))
# data_frame_TLB_noMisses = pd.DataFrame(kernels_time.get("TLB_noMisses"))
print(data_serie_kernel)
print(sorted_df)
# sns.barplot(data = data_serie_kernel, 
#              # x='default', y='TLB_noMisses'
#             )

sorted_df = sorted_df.drop(columns="MPKI")
fig, ax = plt.subplots(constrained_layout=True)

key_list = sorted_df.columns.to_list()
xticklabels = sorted_df.index.to_list()

cat_spacing = 0.5
bar_width = (1 - cat_spacing) / len(key_list)

index = np.arange(len(xticklabels))

# Plot bars
for i, key in enumerate(key_list):
    value = sorted_df[key]
    ax.bar(index + i * bar_width, value, width=bar_width, label=key)

# ax.set_ylim(0, 0.000000004500)
ax.set_xticks(index + bar_width / 2 * (len(key_list) - 1))
ax.set_xticklabels(xticklabels)
ax.set_xlabel('Samples')
ax.set_ylabel('Kernel Time')
ax.legend(title='Directories')

plt.savefig("example.pdf")
#plt.show()