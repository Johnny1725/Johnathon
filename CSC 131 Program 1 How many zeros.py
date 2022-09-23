##Johnathon Terry
##12/10/2019
##Program 1 How Many Zeros
##Python 2.7
##########################################
from time import time

##this finds the number you want to count to
n = input("What is the number do you want to count zeros to?")
##starts timer
start = time()
##function that is called upon to get the zeros 
def get_zeros(n):
    a = 0
    zeros = 0
    ##loop that takes the number you want from one to the number n
    for a in range(1, n+1):
        ##tells the code to repeat until the number is not greater than zero
        while(a > 0):
            ##module that tells if the number has a zero in it or not
            if (a % 10 == 0):
                ##counts the zeros
                zeros = zeros +1
            a //= 10
    return zeros
                
            
            
        
zeros = get_zeros(n)
##stops timer
stop = time()

##prints how many zeros and the time it took to find the zeros
print "The number of zeros written from 1 to {} is {}.".format(n, zeros)
print "This took {} seconds.".format(stop - start)
