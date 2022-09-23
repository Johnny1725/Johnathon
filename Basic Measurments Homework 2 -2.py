import matplotlib.pyplot as plt
import numpy as np

#number of readings and there outputs
x1 = [1,2,3,4,5,6,7,8,9,10]
y1 = [923,932,908,932,919,916,927,931,926,923]

#actual value
V_t = 912

#Finds the average of the data set
V_avg = np.mean(y1)

#Finds the Systematic Error and rounds it to 3 decimal places
SE = abs(V_avg - V_t)
print("The Systematic error is ")
print(round(SE,3))
#Finds the random error and rounds it to 3 decimal places
RE = abs(max(y1) - V_avg)
print("The Random error is ")
print(round(RE,3))
#creates the plot
fig, (ax1) = plt.subplots(1,1)
plt.title('Force Load Acting on a Beam')

ax1.plot(x1,y1, linestyle = 'dashed', marker = '.', color = 'r')
ax1.set_ylabel('Force(n)')
ax1.set_xlabel('Readings')

plt.tight_layout()
plt.show()
