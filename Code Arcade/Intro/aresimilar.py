def solution(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2
#This checks if you can have the same array just from swapping two elements or less. 

print(list(zip([1,2,3,4],[5,6,7,8])))

'''PRACTICE LIST OPERATORS '''


def solution(a, b):
    same_items = sorted(a) == sorted(b)
    differences = [i for i in range(len(a)) if a[i] != b[i]]
    return len(differences) <= 2 and same_items


def solution2(A, B):

    r = []
    for i in range(len(A)):
        if A[i] != B[i]:
            r.append([A[i],B[i]])
            
    if len(r) == 0 or len(r) == 2 and r[0]==r[1][::-1]:
        return True
    return False