import matplotlib.pyplot as plt
import numpy as np
import sys

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html

# data from https://allisonhorst.github.io/palmerpenguins/

base_directory = "/gpfs/projects/bsc18/bsc125019/mgpusim/samples/"

# We have to add matrixtranspose and stencil2d

benchmarks = ["conv2d", "matrixmultiplication", "im2col", "bfs", "spmv", "kmeans", "nbody", "atax", "nw"]

percentil0_list = []
percentil1_list = []
percentil10_list = []
percentil25_list = []
percentil100_list = []
percentil1000_list = []
percentil2000_list = []
percentil5000_list = []

for sample in benchmarks:
    # ParseTouches funcionality
    f = open( base_directory + sample + "/" + sys.argv[1] + "/mem.trace", "r")
    outF = open(base_directory + sample + "/" + sys.argv[1] + "/page_touches.txt" , "w")

    for line in f:
        if "No_touches" in line:
            outF.write(line)
    outF.close()
    f.close()

    # count_touches funcionality

    file = open(base_directory + sample + "/" + sys.argv[1] + "/page_touches.txt" , "r")
    total_lines = 0.0
    percentil0 = 0.0
    percentil1 = 0.0
    percentil10 = 0.0
    percentil25 = 0.0
    percentil100 = 0.0
    percentil1000 = 0.0
    percentil2000 = 0.0
    percentil5000 = 0.0
    for line in file:
        total_lines= total_lines+1
        if int(line.split(",")[4].split(":")[1]) >= 5000:
            percentil5000+=1
        elif int(line.split(",")[4].split(":")[1]) >= 2000:
            percentil2000+=1
        elif int(line.split(",")[4].split(":")[1]) >= 1000:
            percentil1000+=1
        elif int(line.split(",")[4].split(":")[1]) >= 100:
            percentil100+=1
        elif int(line.split(",")[4].split(":")[1]) >= 25:
            percentil25+=1
        elif int(line.split(",")[4].split(":")[1]) >=10:
            percentil10+=1
        elif int(line.split(",")[4].split(":")[1]) >= 1:
            percentil1+=1
        elif int(line.split(",")[4].split(":")[1]) == 0:
            percentil0+=1
    #include percentil to the list divided by total_lines
    if (total_lines == 0):
        print("Error: " + sample + " has 0 lines")
    if(percentil0 == 0):
        percentil0_list.append(0)
    else:
        percentil0_list.append(percentil0/total_lines)
    if(percentil1 == 0):
        percentil1_list.append(0)
    else:
        percentil1_list .append(percentil1/total_lines)
    percentil10_list.append(percentil10/total_lines)
    if(percentil25 == 0):
        percentil25_list.append(0)
    else:
        percentil25_list.append(percentil25/total_lines)
    if(percentil100 == 0):
        percentil100_list.append(0)
    else:
        percentil100_list.append(percentil100/total_lines)
    if(percentil1000 == 0):
        percentil1000_list.append(0)
    else:
        percentil1000_list.append(percentil1000/total_lines)
    if(percentil2000 == 0):
        percentil2000_list.append(0)
    else:
        percentil2000_list.append(percentil2000/total_lines)
    if(percentil5000 == 0):
        percentil5000_list.append(0)
    else:
        percentil5000_list.append(percentil5000/total_lines)
    file.close()


# species = (
#     "Adelie\n $\\mu=$3700.66g",
#     "Chinstrap\n $\\mu=$3733.09g",
#     "Gentoo\n $\\mu=5076.02g$",
# )
species = benchmarks
weight_counts = {
    "0": np.array(percentil0_list),
    "1-9": np.array(percentil1_list),
    "10-24": np.array(percentil10_list),
    "25-99": np.array(percentil25_list),
    "100-999": np.array(percentil100_list),
    "1000-1999": np.array(percentil1000_list),
    "2000-4999": np.array(percentil2000_list),
    "5000+": np.array(percentil5000_list),
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(len(benchmarks))

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Distribution of page touches")
ax.legend(loc="upper right")

plt.show()
plt.savefig("stackedBar_touches.pdf")
