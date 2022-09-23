
##############################################
##Johnathon Terry
##12/16/19
##Program 2: Sort Comparison and Swaps
##############################################
#Takes the and makes it a function that we can call upon
def getList():
    List = [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]
    return List
#Takes the list and sorts it in the Bubble Sort
def bubbleSort(List):
    swaps = 0
    comps = 0
    for a in range (0, len(List) - 1):
        for x in range (0, len(List) - 1 - a):
            comps += 1
            if List[x] > List[x + 1]:
                List[x], List[x + 1] = List[x + 1], List[x]
                swaps += 1
    return comps, swaps
        
#Takes the list and sorts it in the Optimized Bubble Sort    
def optimizedBubbleSort(List):
    comps = 0
    repeat = True
    swaps = 0
    x = len(List)
    z = 0
    while (x > 1 and repeat == True):
        repeat = False
        
        for a in range(len(List) - z - 1):
            comps += 1
            #a comparison is abpout to occur, increment it
            if List[a] > List[a + 1]: 
                List[a],List[a+1] = List[a + 1],List[a]
                swaps += 1
                repeat = True    
        x -= 1
        z += 1

    return comps, swaps

#Takes the list and sorts in the Selection Sort
def selectionSort(List):
    comps = 0
    swaps = 0
    for a in range (0, len(List) - 1): 
        minIndex = a
        for x in range(a + 1, len(List)):
            comps += 1
            if List[a] < List[minIndex]:
                minIndex = x
        List[a], List[minIndex] = List[minIndex], List[minIndex]
        swaps += 1
    return comps, swaps

#Takes the list and sorts it in the insertion sort
def insertionSort(List):
    comps = 0
    swaps = 0
    for a in range (0, len(List)):
        comps += 1
        minIndex = List[a]
        for x in range(a -1, 0, -1):
            if List[x] > minIndex:
                List[x + 1] = List[x]
                swaps += 1
            else:
                List[x + 1] = minIndex
                break
    return comps, swaps


#################################################
##Main part of the code where the functions are called upon and used to find the list sorted, how many comparisons, how many swaps the
##each type of sort made
List = getList()
print"Original List {}".format((List))
comps, swaps = bubbleSort(List)
print"After Bubble Sort {}".format(List)
print"{} comparisons; {} swaps".format(comps, swaps)
print


List = getList()
print"Original List {}".format((List))
comps, swaps = optimizedBubbleSort(List)
print "After Optimized Bubble Sort {}".format(List)
print "{} comparisons; {} swaps".format(comps, swaps)
print

List = getList()
print"Original List {}.".format(List)
comps, swaps = selectionSort(List)
print "After Selection Sort {}".format(List)
print"{} comparisons; {} swaps".format(comps, swaps)
print

List = getList()
print"Original List {}".format(List)
comps, swaps = insertionSort(List) 
print "After Insertion Sort {}".format(List)
print "{} comparisons; {} swaps".format(comps, swaps)


        
