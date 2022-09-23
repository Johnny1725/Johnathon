import csv
import matplotlib.pyplot as plt
from collections import Counter
import statistics
import scipy.stats as stats
import numpy as np
import math

# The name of the csv file
filename = 'WinningNumbers.csv'

# Open then read the file, and remove any whitespaces before/after the file
file = open(filename).read()

# Split the file by each newline
rows = file.split('\n')

# Remove the header (the first row)
rows.pop(0)

# Create a variable to store all the winning numbers
cells = []

# Loop through each row
for row in rows:   
    # Split the row by each comma
    temp = row.split(',')
      
    # Add the winning numbers to the cells variable but do not include the date.
    # Note: The [1:] is call list slicing.
    # https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
    cells.extend(temp[1:])
    
# Make all the cells values integers and not strings using list comprenhension
# https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
cells = [int(cell) for cell in cells]

print(cells)

i = 0
cell = []
x = 0
y = 0
z = 0

while(i < len(cells)-1):
    x = str(cells[i])
    y = str(cells[i+1])
    z = str(cells[i+2])
    t = int(x+y+z)
    cell.append(t)
    i += 3
    
print(cell)
    
r = [0,1000]
bin = 9
        
fig, ax = plt.subplots(1,1)

#ax.hist(cell, bin, r, color='green', histtype='bar', rwidth=0.8)

#ax.set_xlim(r)

#ax.set_xlabel('Winning Numbers')
#ax.set_ylabel('Number of Winning Numbers')
#ax.set_title('My histogram')

mean = statistics.mean(cell)
mode = statistics.mode(cell)
median = statistics.median(cell)
sample_mean = statistics.mean(cell)
stdev = statistics.stdev(cell)
pmean = statistics.mean(cell)
pstdev = statistics.pstdev(cell)

print("Mean is : ", mean)
print("Median is : ", median)
print("Mode is : ", mode)
print("Sample Mean is : ", sample_mean)
print("Standard Deviation is: ", stdev)
print("Population Mean is : ", pmean)
print("Population Standard Deviation", pstdev)

h = sorted(cell)

fit=stats.norm.pdf(h, np.mean(h), np.std(h))
plt.plot(h, fit, '.')

plt.show()
        
