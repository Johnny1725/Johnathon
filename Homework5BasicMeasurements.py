import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat
import numpy as np
import scipy.stats as sp
import random
 

fig, weightfat = plt.subplots(1,1)
fig, heightfat = plt.subplots(1,1)
fig, neckthighbicepfat = plt.subplots(1,1)
fig, sixfat = plt.subplots(1,1)
fig, sevfat = plt.subplots(1,1)
data = pd.read_excel('body_fat.xlsx')


body_fat=[]
weight=[]
height=[]
neck=[]
thigh=[]
bicep=[]
age=[]


bodyfat=data['BODYFAT']

 
weight=data['WEIGHT']
height=data['HEIGHT']
neck=data['NECK']
thigh=data['THIGH']
bicep=data['BICEPS']
age=data['AGE']
 

weightfat.scatter(weight,bodyfat)
weightfat.set_xlabel('WEIGHT (lbs)')
weightfat.set_ylabel('BODYFAT (%)')
heightfat.scatter(height,bodyfat)
heightfat.set_xlabel('HEIGHT (in)')
heightfat.set_ylabel('BODYFAT (%)')
neckthighbicepfat.scatter(thigh,bodyfat,label='thigh')
neckthighbicepfat.scatter(bicep,bodyfat,label='bicep')
neckthighbicepfat.scatter(neck,bodyfat,label='neck')
neckthighbicepfat.set_xlabel('NECK, THIGH, and BICEPS diameter (in)')
neckthighbicepfat.set_ylabel('BODYFAT (%)')
neckthighbicepfat.legend()
 

body_fat.sort()

pop_mean = stat.mean(bodyfat)
print("Mean:" , pop_mean)
num_median = stat.median(bodyfat)
print("Median:" , num_median)
num_mode = 19
print("Mode:" , num_mode)


sixty=data.loc[(data['AGE']>=60) & (data['AGE']<70)]
smean = stat.mean(sixty['BODYFAT'])
sixdev = stat.stdev(sixty['BODYFAT'])
print("smaple mean: ", smean)
print("sample standard deviation: ", sixdev)
 
 
lower6 = smean - 4*sixdev
upper6 = smean + 4*sixdev
x = np.linspace(lower6, upper6, 100)


dist6 = sp.norm(smean, sixdev)


sixfat.plot(x, dist6.pdf(x))
sixfat.set_title('Body Fat Distribution for men 60-69')
 
seventy = data.loc[(data['AGE'] >=70) & (data['AGE'] < 80)]
sevmean = stat.mean(seventy['BODYFAT'])
sevdev = stat.stdev(seventy['BODYFAT'])
print("sample mean: ", sevmean)
print("sample stadard deviation: ", sevdev)
 
lower7 = sevmean - 4*sevdev
upper7 = sevmean + 4*sevdev
x7 = np.linspace(lower7, upper7, 100)
 
dist7 = sp.norm(sevmean, sevdev)
sevfat.plot(x7, dist7.pdf(x7))
sevfat.set_title('Body Fat Distribution for men 70-79')
 
plt.tight_layout()
plt.show()