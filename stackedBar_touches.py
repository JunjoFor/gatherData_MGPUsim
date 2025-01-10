import matplotlib.pyplot as plt
import numpy as np
import sys

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html

# data from https://allisonhorst.github.io/palmerpenguins/

base_directory = "../mgpusim/samples/"

benchmarks = ["conv2d", "matrixmultiplication", "im2col", "bfs", "spmv", "kmeans", "nbody", "atax", "nw", "matrixtranspose", "stencil2d"]

percentil0 = []
percentil1 = []
percentil10 = []
percentil25 = []
percentil100 = []
percentil1000 = []
percentil2000 = []
percentil5000 = []
i = 0
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
    total_lines = 0
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


species = (
    "Adelie\n $\\mu=$3700.66g",
    "Chinstrap\n $\\mu=$3733.09g",
    "Gentoo\n $\\mu=5076.02g$",
)
weight_counts = {
    "Below": np.array([70, 31, 58]),
    "Above": np.array([82, 37, 66]),
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")

plt.show()