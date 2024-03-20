def solution(inputArray, k):
    indexpointer = k-1
    for loop in range(len(inputArray)//k):
        inputArray.pop(loop*k+indexpointer)
        indexpointer-=1
    return inputArray

'''
    Here what i do is i set the initial pointer to the kth element (offset by 1 to ensure 0-indexing)
    then we loop around (length of the array divided by k ignoring remainder) to ensure we remove all 
    multiples of k elements in the queue. We remove the first element by using pop, then decrease our 
    pointer by one as we already removed an item from the list to compensate for the lost item.
    Then we loop but move up by the loop number amount of k :) 
'''

def solution2(inputArray, k):
    del inputArray[k-1::k]
    return inputArray


'''
    Here is an ever-simpler solution, where we take the input array and delete all multiples of k's from the queue, starting with k-1.
    Bruh
'''