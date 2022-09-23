# name = "Johnathon"
# print ("Hello, " + name + ".")
# 
# print ("")
# 
# print ("I can count to a thousand by fives. Watch me count.")
# 
# i = 0
# 
# while(i <= 1000):
#     print (i)
#     i += 5
# import matplotlib.pyplot as plt
# 
# x1 = [2, 3, 4, 5]
# y1 = [9, 4, 3, 2]
# x2 = [11, 20, 30, 50]
# y2 = [20, 30, 50, 60]
# 
# fig, (ax1, ax2)  = plt.subplots(1,2)
# 
# plt.title('Problem 5 Figure Title')
# 
# ax1.set_xlabel('problem 5 x1 data')
# ax1.set_ylabel('problem 5 y1 data')
# 
# ax1.plot(x1,y1, color = 'red', linestyle='dashdot',linewidth=1, marker='o')
# ax2.plot(x2,y2, label = 'x2,y2', color = 'red', linestyle='solid', marker='o')
# ax2.plot(y1,y2, label = 'y1,y2', color='yellow', linestyle='dashdot', marker='o' )
# 
# ax2.set_xlabel('problem 5 x2 data')
# ax2.set_ylabel('problem 5 y2 data')
# 
# ax1.legend()
# ax2.legend()
# plt.tight_layout
# 
# plt.show()
import matplotlib.pyplot as plt

activities = ['you try to guess and you get it right', 'You try to guess and you get it wrong', 'You wait for someone else to say the name']
Percents = [2, 5, 93]

sector_color = ['r', 'b', 'g']

fig, ax = plt.subplots(1, 1)

ax.pie(Percents, labels=activities, colors=sector_color, explode=[0.3,0,0], radius=1.2)

ax.set_title('When You Forget Someones Name')

ax.legend()

plt.show()




    
    