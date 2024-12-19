import sys
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import hmean


aux = pd.read_csv(sys.argv[1])

CumCPI = 0.0
numCPI = 0.0
for i, j in aux.iterrows():
    if j[' what'] == ' cu_CPI':
        CumCPI = CumCPI + float(j[' value'])
        numCPI = numCPI + 1

print("El CPI medio es: " + str(CumCPI/numCPI))

