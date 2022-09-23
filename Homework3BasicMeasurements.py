import matplotlib.pyplot as plt
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [923, 932, 908, 932, 919, 916, 927, 931, 926, 923]

fig, (ax1) = plt.subplots(1,1)
plt.title("Force Load Acting on a Beam")

ax1[0,0].plot(x1, y1, linestyle='dashed', marker = '.', color='r')
ax1[0,0].set_ylabel('Forces (N)')
ax1[0,0].set_xlabel('Readings')

plt.tight_layout()

plt.show()