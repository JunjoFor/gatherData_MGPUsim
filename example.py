import sys
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import hmean


# Parsing folders

samplesUsed = ["conv2d", "matrixmultiplication", "im2col", "bfs", "spmv", "kmeans", "nbody", "nw"]
secondDir = ["default_fixTLB", "TLB_noMisses_fixTLB"]
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
        kernels_time["Instructions"][sample] = 0.0
        kernels_time["TLB_misses"][sample] = 0.0

for directory, samples in metrics.items():
    for sample in samples:
        dict_metrics = metrics.get(directory)
        aux = dict_metrics.get(sample)
        for i, j in aux.iterrows():
            if j[' what'] == ' kernel_time' and j[' where'] == ' Driver':
                kernels_time[directory][sample] = float(j[' value'])
            if directory == "default_fixTLB" and j[' what'] == ' cu_inst_count':
                kernels_time["Instructions"][sample] = kernels_time["Instructions"][sample] + float(j[' value'])
            component = j[' where'].split(".")
            if len(component) > 2:
                if directory =="default_fixTLB" and ("TLB" in component[2]) and j[' what'] == ' miss':
                    kernels_time["TLB_misses"][sample] = kernels_time["TLB_misses"][sample] + float(j[' value'])
            

data_serie_kernel = pd.DataFrame(kernels_time)

data_ipc = pd.DataFrame()
default_value = 0.0
tlbNoMisses_value = 0.0
for row in data_serie_kernel.itertuples(index=True):
    if row.default_fixTLB > 0 and row.TLB_noMisses_fixTLB > 0:
        data_ipc.loc[row[0], 'default_fixTLB'] = row.default_fixTLB / row.default_fixTLB
        data_ipc.loc[row[0], 'TLB_noMisses_fixTLB'] = row.default_fixTLB / row.TLB_noMisses_fixTLB
        if row.Instructions <= 0:
            data_ipc.loc[row[0], "MPKI"] = 0.0
        else:
            data_ipc.loc[row[0], "MPKI"] = row.TLB_misses / (row.Instructions/1000.0)
    
sorted_df = data_ipc.sort_values(by="MPKI", ascending=False)

# data_frame_default = pd.DataFrame(kernels_time.get("default"))
# data_frame_TLB_noMisses_fixTLB = pd.DataFrame(kernels_time.get("TLB_noMisses_fixTLB"))
print(data_serie_kernel)
print(sorted_df)
# sns.barplot(data = data_serie_kernel, 
#              # x='default', y='TLB_noMisses_fixTLB'
#             )

sorted_df = sorted_df.drop(columns="MPKI")

harmonic_means = sorted_df.apply(hmean)
print("Hmean : ", harmonic_means)
sorted_df.loc['Hmean'] = harmonic_means
fig, ax = plt.subplots(constrained_layout=True)

key_list = sorted_df.columns.to_list()
xticklabels = sorted_df.index.to_list()

cat_spacing = 0.2
bar_width = (1 - cat_spacing) / len(key_list)

index = np.arange(len(xticklabels))

# Plot bars
for i, key in enumerate(key_list):
    value = sorted_df[key]
    ax.bar(index + i * bar_width, value, width=bar_width, label=key)

# ax.set_ylim(0, 0.000000004500)
ax.set_xticks(index + bar_width / 2 * (len(key_list) - 1))
ax.set_xticklabels(xticklabels, rotation=90)
# ax.set_xlabel('Samples')
ax.set_ylabel('SpeedUp')
ax.legend(title='Directories')

plt.savefig("SpeedUp_noMisses_fixTLB_sorted.pdf")
# plt.show()