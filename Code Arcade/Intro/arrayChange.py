def solution(inputArray):
    counter = 0
    for loop in range(1,len(inputArray)):
        while(inputArray[loop-1]>=inputArray[loop]):
            difference = inputArray[loop-1]-inputArray[loop]
            inputArray[loop] += difference+1
            counter+=difference+1
    return counter

def solution2(inputArray):
    sum([])

print(solution([1,1,1]))

''' 
    Issue here was that the program was taking too long to execute.
    This was solved by miniming loop time, as previously it was going 
    to loop as long as the total sum of all numbers in the array.
    Now the total loop number has been changed to the length of the 
    array.
'''