#My original version:
def solution(n, firstNumber):
    listOfNums = list(range(0, n))
    index = int((firstNumber+(n/2))%n)
    return listOfNums[index]

#Simpler version:
def solution(n, firstNumber):
    return (firstNumber + n/2)%n

#Wow, nice