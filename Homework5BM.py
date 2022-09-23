# Name: Johnathon Terry
# Date: October 24, 2020
# Homework 5

import matplotlib.pyplot as plt
import pandas as pd
import statistics as statistics
import numpy as np
import scipy.stats as stats
import random

data = pd.read_csv('bodyfat.csv',delimiter = ',')
data.head()
f1 = plt.figure(figsize = (15,5))

y = data[["BODYFAT"]]
x = data[["WEIGHT"]]
ax1 = f1.add_subplot(1,3,1)
ax1.scatter(x,y, color = "b", marker = 'o')
ax1.set_xlabel('Weight (lbs)')
ax1.set_ylabel('Bodyfat %')
ax1.set_title('Bodyfat vs. Weight')
ax1.grid(True)

y = data[["BODYFAT"]]
x = data[["HEIGHT"]]
ax2 = f1.add_subplot(1,3,2)
ax2.scatter(x,y, color = "r", marker = 'o')
ax2.set_xlabel('Height (in)')
ax2.set_ylabel('Bodyfat %')
ax2.set_title('Bodyfat vs. Height')
ax2.grid(True)


y = data[["BODYFAT"]]
x = data[["NECK"]]
x2= data[["THIGH"]]
x3= data[["BICEPS"]]

# for i in range(0,len(y)-1):
#     if(y[i]>y[i+1]):
#         (y[i], y[i+1]) = (y[i+1], y[i])
        


print(y[0])
ax3 = f1.add_subplot(1,3,3)
ax3.scatter(x,y,label = 'Neck', color = "magenta", marker = 'o')
ax3.scatter(x2,y,label = 'Thigh', color = "green", marker = 'o')
ax3.scatter(x3,y,label = 'Bicep', color = "orange", marker = 'o')
ax3.set_ylabel('Bodyfat %')
ax3.set_title('Bodyfat vs. Neck,Thigh,Biceps')
ax3.grid(True)
ax3.legend()




plt.tight_layout()
plt.show()