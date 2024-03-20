'''
    From what I understand, here we need to find the smallest number 
    for which all of the numbers in the array are not divisible by 
    (without a remainder) - This way we can make sure that you can make 
    hops of that multiple to make it through all the obstacles.

    I think that when looking at the list, we can eliminate all the
    prime factors.
    
'''
def solution(inputArray):
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1
'''
    Okay, wrong approach. What they are doing here is they start with 
    c as 2, as every number is a multiple of 1. Then they run an infinite loop
    (dangerous potentially - as it might stop within the max number of elements 
    in the list) that sorts a list created by finding the lowest
    remainder from a division by c for every element in the list. 
    If the lowest remaineder happens to be above zero, then every element in the 
    list is not a multiple of the number, meaning that C can be used to hop through
    all the elements in the list and not come across any numbers in the list in 
    its journey. 

'''
print(solution([1,2,3,4,5]))

def solution2(inputArray):
    i=2
    while True:
        if all(x%i!=0 for x in inputArray):
            return i
        i=i+1
            
'''
    Here is another, that begins with c= 2, and check if all the numbers
    in the list divided by c leave a remainer. If they don't it means you
    can hop through with it.
'''