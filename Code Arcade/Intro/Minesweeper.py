import numpy
def solution(matrix):
    matrix2 = numpy.zeros((len(matrix),len(matrix[0])))
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            print("Now on",x,",",y)
            mines = 0
            for loop1 in range(-1,2):
                for loop2 in range(-1,2):
                    if loop1 == 0 and loop2 == 0:
                        continue
                    elif loop1+x < 0 or loop1+x >= len(matrix) or loop2+y<0 or loop2+y >= len(matrix[0]):
                        continue
                    if matrix[x+loop1][y+loop2] == True:
                        print("adding 1 to",x,",",y,"because" ,x+loop1,",",y+loop2,"has a mine")
                        print("Does ",matrix[x+loop1][y+loop2],"really equal True?")
                        mines += 1
            matrix2[x][y] = mines
    return matrix2

'''
    Okay, this code didn't work because I was silly.
    For some reason when declaring a matrix you should probably reset it all,
    instead of copying it.

    TLDR... Instead of matrix2 = matrix
            Write matrix = numpy.zeros((len(matrix),len(matrix[0])))
'''