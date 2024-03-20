def solution(a):
    distances = []
    for num in a:
        dist = 0
        for number in a:
            dist += abs(num-number)
        distances.append(dist)
    return sorted(zip(distances,a),key = lambda distance: distance[0])[0][1]

'''
    here i am trying to find number with smallest average distance from all other numbers.

    Here i understand it is in ascending order, therefore using the length of the array divided by two,
    ignoring the remainer, we are left with the 'middle' value.
    Then what we can do select either that value or the one to the right, by using the remainder of the division.
    Simple.
    Even simpler is to use the length of A minus one, then find the middle, which eliminates the need for the use of
    the remaineder later on.

'''

def solution2(A):
    return A[len(A)//2-(len(A)%2==0)]

def solution3(A):
    return A[(len(A)-1)//2]
