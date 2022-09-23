from time import time


def example1(S):
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total

def example2(S):
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total

def example3(S):
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += S[k]
    return total

def example4(S):
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total


##if __name__ == "__main__":
##
##    start_time = time()
##    S = range(100000)
##    example1(S)
##    end_time = time()
##    T_time = end_time - start_time
##    print("Execution 1 time = {}".format(T_time))
##
##if __name__ == "__main__":
##    start_time = time()
##    S = range(100000)
##    example2(S)
##    end_time = time()
##    T_time = end_time - start_time
##    print("Execution 2 time = {}".format(T_time))
##
##if __name__ == "__main__":
##    start_time = time()
##    S = range(100000)
##    example3(S)
##    end_time = time()
##    T_time = end_time - start_time
##    print("Execution 3 time = {}".format(T_time))
##
##if __name__ == "__main__":
##    start_time = time()
##    S = range(100000)
##    example4(S)
##    end_time = time()
##    T_time = end_time - start_time
##    print("Execution 4 time = {}".format(T_time))

###### 2 #################
class Progression(object):
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self,n):
        print(' '.join(str(next(self)) for j in range(n)))
class ArithmeticProgression(Progression):
    def__init__(self,increment = 1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):          #####Needs an _ before advance
        self._current += self._increment ####This was backwards

if __name__ == '__main__':
    a = ArithmeticProgression(2,1)
    print(" ".join(str(next(a)) for _ in range(10))) ###Where the _ is you need
                                                        # a vairable
    
        
class AbsoluteProgression(Progression):

    def __iter__(self):
        return self
    
    def __init__(self, increment=2, start=200):
        super(AbsoluteProgression, self).__init__(start)
        self._increment = increment

    def _advance(self):
        self._current = self._current - self._increment
        print(abs(self._current))

    
if __name__ == '__main__':
    AbsoluteProgression()._advance()

######### 3 #################

n = range(1,10)


i = len(n) 

j = 0
a = range(1,10)

b = 0
c = 0
while j < i:
    a[c] = pow(n[j],2)
    b += a[j]
    j += 1
    c += 1
print b

#I got summ by taking a sum of the squares of the First n
summ = i*(i+1)*(2*i+1)/6
#print summ

############# 4 $$$$$$$$$$$$$$$$
import math

n = range(1,9)
s1 = range(1,9)
s2 = range(1,9)
i = len(n)
j = 0
summ1 = 0
while j < i:
    s1[j] = math.log(n[j],10)
    summ1 += s1[j]
    j += 1

summ2 = n[i-1]*math.log(n[i-1],10)
    
#print summ1
#print summ2

############ 5 ####################### Describe!!!!!!!!!!
a = 0

def count(n,a):
    if n >= 1:
        count(n-1)
        summ = a + 1
        summ += summ
        print summ
        count(n-1)
 
#count(4,a)

def count(n,c,d,i):
    if(n = 0):
        print("move disk from current poition to destination")

    else:
        count(n-1, c, i,d)
        move(c,d)
        count(n-1,i,d,c)

def move(c,d):
    print("move disk from", c, "to", d)



############ 6 #####################

def clear(S):
    if S == []:
        return []
    elif not instance(S[0], list):
        return remove_words(S[1:])


############# 8 ###################
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        temp = self.head
        while(temp):
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

L = LinkedList()
L.insert(3)
L.insert(4)
L.insert(5)
L.reverse()
L.printLL()


class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        temp = self.head
        while(temp):
            print(current.data)
            current = current.next

    def reverse(self):
        

def __init__(self, start=0):
    raise StopIteration()

