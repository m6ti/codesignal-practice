'''
    hash tables from the previous one are out the picture.
    What we need here is an efficient method of checking if the character in the array is the
    first not repeating character.

    We can use if array.index(c) == array.rindex(c)
                    to see if it is only one occurence in the string
'''