def solution(inputArray, k):
    return max([sum(inputArray[x:k+x])for x in range(0,len(inputArray)-k+1)])

print("solution:",solution([2, 3, 5, 1, 6],2))

'''
    This code is for how to pick the max number of a consecutive number of elements 
    in an array
'''
#My solution ^^ Works, but is too slow. :(

def solution2(inputArray, k):
    max = 0
    looper= 0
    for loop in range(len(inputArray)-k+1):
        
        #print(sum(inputArray[looper:k+looper]))
        if sum(inputArray[looper:k+looper])>max:
            max = sum(inputArray[looper:k+looper])
        looper+=1
    return max

def solution3(inputArray, k):
    tempSum = sum(inputArray[0:k])
    #Temporary sum is max sum at first of first k numbers
    maxSum = tempSum
    for i in range(k, len(inputArray)):
        
        tempSum = tempSum - inputArray[i-k] + inputArray[i]
        maxSum = max(maxSum,tempSum)
    return maxSum