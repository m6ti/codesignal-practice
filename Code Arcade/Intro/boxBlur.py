import math
def solution(image):
    solutionImage  = [[0 for _ in range(len(image[0])-2)]for __ in range(len(image)-2)]
    print(solutionImage)
    for y in range(1,len(image[0])-1):
        for x in range(1,len(image)-1):
            sums = 0
            for loop1 in range(-1,2,1):
                for loop2 in range(-1,2,1):
                    sums += image[x+loop1][y+loop2]
            print("averaging",x-1,",",y-1,"as",sums/9)
            solutionImage[x-1][y-1]= math.floor(sums/9)
            print("eroo")
    return solutionImage

'''
    Remember that x and y are swapped when referencing as solutionimage[1][2] your really accessing [2,1] in the matrix.
'''