#################################################
####Name: Johnathon Terry
####Date: 2/7/2020
####Program: Program 6: A Foolproof Game
###################################################
from random import randint

#simulates the flip of the coin
def flip():
    return randint(1, 2)

#get the number of games and the amount of flips per game
num_games = input("How many games?")

num_tosses = input("How many coin tosses per game?")


#flip the dice
prof_W = 0
groupB_W = 0
groupA_W = 0
game = 0
#forloop that has a range from zero to the number of games you choose
for i in range(0, num_games):
    groupA = 0
    groupB = 0
    prof = 0
    groupA_P = 0
    #forloop that has a range from zero to the number of tosses you chose to have
    for i in range(0, num_tosses):
        flip1 = flip()
        flip2 = flip()
        #Tells us who wins the flip
        if (flip1 == 1 and flip2 == 1):
            groupA += 1
        else :
            if (flip1 == 2 and flip2 == 2):
                groupB += 1
            else :
                prof += 1

        #changes the amount of flips each group/professor into percentages         
        groupA_P = (float(groupA)/num_tosses)*100.00
        groupB_P = (float(groupB)/num_tosses)*100.00
        prof_P = (float(prof)/num_tosses)*100.00

    #Tells us who wins the game, which is determined by who gets the most flips
    if (groupA > groupB and groupA > prof):
        groupA_W += 1
    else:
        if (groupB > groupA and groupB > prof):
            groupB_W += 1
        else:
            prof_W += 1
            
    #changes the amount of wins of each group/professor into percentages
    groupA_W_P = (float(groupA_W)/num_games)*100.00
    groupB_W_P = (float(groupB_W)/num_games)*100.00
    prof_W_P = (float(prof_W)/num_games)*100.00

    #prints which games its on and then increases that number by 1 every loop
    print "Game {}:".format(game)
    game += 1
    #prints the statement that tells us how many flips each group/professor got 
    print "  Group A: {} ({}%) ; Group B: {} ({}%); Prof: {} ({}%)".format(groupA,round(groupA_P, 2), groupB, round(groupB_P, 2), prof, round(prof_P, 2))
#prints the statement that tells us how many games each group/professor got 
print "Wins: Group A = {} ({}%), Group B = {} ({}%), Prof = {} ({}%)".format(groupA_W, round(groupA_W_P, 2), groupB_W, round(groupB_W_P, 2), prof_W, round(prof_W_P, 2))

            
        

    
        

    
    




