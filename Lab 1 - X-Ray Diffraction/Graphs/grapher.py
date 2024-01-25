"""
Created on Thu Jan 25 14:00:01 2024

@author: Matthew Culbertson
"""
#import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Data Importation.
filename = "ZeroData"
data = pd.read_csv("./Data/" + filename + ".csv", sep=",") 
y = np.array(data['rate']) #per second
x = np.array(data['angle'])
y = y.astype(float)
x = x.astype(float)

#variables
maintitle = "Count Rate Vs Angle" 
xtitle = "Angle"
ytitle = "Counts Per Second"
xticksize = 0.5
yticksize = 500
xmin = min(x)
ymin = 0 #min(y)
xmax = max(x)
ymax = max(y)

plt.plot(x, y)
plt.xlabel(xtitle) 
plt.ylabel(ytitle)
plt.xticks(np.arange(xmin, xmax+xticksize, xticksize))
plt.yticks(np.arange(ymin, ymax+yticksize, yticksize))
ax = plt.gca()
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
plt.title(label = maintitle)
plt.grid()
plt.show()

