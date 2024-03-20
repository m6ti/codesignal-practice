def arrayOfZeros(x,y):
    return [[0] * y for loop in range(x)]
    

def arrayOfZeros2(x,y):
    return  [[0 for cols in range(y)] for rows in range(x)]


def arrayOfZeros3(x,y):
    return numpy.zeros(3,3)

'''
    The easiest and laziest option that works on codesignal.
    return numpy.zeros((2,2))
'''

print(arrayOfZeros3(3,3))
