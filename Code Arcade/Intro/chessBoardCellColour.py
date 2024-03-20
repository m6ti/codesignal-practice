def solution(cell1, cell2):
    if color(cell1)==color(cell2):
        return True
    else:
        return False
    
#Return 0 if pale, Return 1 if vibrant
def color(cell):
    number1 = ord(cell[0])-65
    number2 = int(cell[1])-1
    even = [0,1,0,1,0,1,0,1]
    odd = [1,0,1,0,1,0,1,0]
    if number1%2!=0:
        return odd[number2]
    else:
        return even[number2]


'''
    I created a function color, that tells me if a cell is white or black on the chess board,
    given its position (e.g. A1, A2, A3 ...).
    So what I did is convert the letter in the position to tell me if it is corresponding to 
    an 'even' (e.g. B, D, F) letter, with the combination of the number in the position, to tell me 
    if it in an 'even' row or a 'odd' row, and then index the rows.

    The problem asks if the cells are the same color, so the solution function simply checks if they are the same colour.
    Nice. 
'''