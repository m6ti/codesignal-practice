import itertools

def solution(inputArray):
    combinations = list(p for p in itertools.permutations(inputArray,len(inputArray)))
    for combination in combinations:
        flag = True
        for loop in range(len(combination)-1):
            if not differByUno(combination[loop],combination[loop+1]):
                flag = False
        if flag == True:
            return True
    return False   
    
    
    
def differByOne(one, two):
    differs = 0
    for instance in zip(one,two):
        if instance[0]!=instance[1]:
            differs+=1
        if differs>1:
            return False
    if differs == 1:
        return True
    else:
        return False

'''
    A simpler approach below.
    Here we can test for differences by simply returning the sum of a list that compares the zipped list and sees
    if the items are the same.
'''


from itertools import permutations

def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

'''
    here ive sneaked in my solution below:
'''

def differByUno(one, two):
    return sum([uno != duo for (uno,duo) in zip(one,two)]) == 1

def solution2(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False

print(solution(["ab", "bb", "aa"]))
