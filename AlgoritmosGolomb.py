from time import time

##############################################################################################################

#Python 3 script to list the first n numbers of the sequence
def golombListGenerator(n):
    
    #unexpected parameter
    if (n <= 0):
        print("Expected positive values (nth position in the sequence, starting at 1)!")
        return 

    GolombSequence = list()
    a_n = 1
    
    #generate list 
    while (len(GolombSequence) < n):
        GolombSequence.append(a_n)
        #add n, (a_n - 1) more times
        for _ in range(GolombSequence[a_n - 1] - 1):
            if (len(GolombSequence) == n): return tuple(GolombSequence)
            GolombSequence.append(a_n)
        a_n += 1

##############################################################################################################

inicio = time()

firstNumbers = 45
print("The first " +str(firstNumbers) + " numbers of the sequence are:\n", golombListGenerator(firstNumbers))

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")

##############################################################################################################

#Python 3 script to find the n-th number of Golomb's sequence
def findNthElement(n):
    
    #unexpected parameter
    if (n <= 0):
        print("Expected positive values (nth position in the sequence, starting at 1)!")
        return

    #recursion stop condition (base)
    elif (n == 1):
        return 1

    return 1 + findNthElement(n - findNthElement(findNthElement(n - 1)))

##############################################################################################################

inicio = time()

searchedIndex = 45
print("The element #" + str(searchedIndex) +  " of the sequence is " + str(findNthElement(searchedIndex)))

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")

##############################################################################################################

#Python 3 script to alternatively find the nth number of the Golomb sequence
#non-recurrent
def alternativefindNthElement(n):
    
    #unexpected parameter
    if (n <= 0):
        print("Expected positive values (nth position in the sequence, starting at 1)!")
        return

    #vector that stores the index of the first occurrence of n
    #indexFirst[n] <- index of the first occurrence of n (starting at 1)
    indexFirst = [1]
    a_n = 2
    temp = int()

    #build index vector
    while True:
        #find how many times n occurs (n occurs a_n times)
        #as we do not know the value of a_n, we look for the index  
        #in the vector indexFirst which encompasses the position a_n
        for lastIndex in indexFirst:
            if lastIndex < a_n : temp = lastIndex
            else: break
        
        #indexFirst[n+1] = indexFirst[n] + how many times n occurs
        nextIndex = indexFirst[-1] + (indexFirst.index(temp)+1)
        
        #stop condition
        if (nextIndex > n): break   

        indexFirst.append(nextIndex)

        a_n += 1
    
    return len(indexFirst)

##############################################################################################################

inicio = time()

searchedIndex = 45
print("The element #" + str(searchedIndex) +  " of the sequence is " + str(alternativefindNthElement(searchedIndex)))

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")

##############################################################################################################

#Python 3 script to find the range of indices where 
#the number n appears in the Golomb's sequence
def indexInterval(n):
    
    if (n <= 0):
        print("Expected positive values (starting at 1)!")
        return
    
    #vector that stores the index of the first occurrence of n
    #indexFirst[n] <- index of the first occurrence of n (starting at 1)
    indexFirst = [1]
    a_n = 2
    temp = int()

    #build index vector
    while True:
        #find how many times n occurs (n occurs a_n times)
        #as we do not know the value of a_n, we look for the index  
        #in the vector indexFirst which encompasses the position a_n
        for lastIndex in indexFirst:
            if lastIndex < a_n : temp = lastIndex
            else: break
        
        #indexFirst[n+1] = indexFirst[n] + how many times n occurs
        #factor 1 appears because array index starts at 0
        nextIndex = indexFirst[-1] + (indexFirst.index(temp) + 1)
        
        #stop condition
        if (len(indexFirst) > n): break   

        indexFirst.append(nextIndex)

        a_n += 1
    
    return tuple(range(indexFirst[-2], indexFirst[-1]))

##############################################################################################################

inicio = time()

n = 12
print("The number " + str(n) +  " occurs in the positions " + str(indexInterval(n)))

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")

##############################################################################################################
