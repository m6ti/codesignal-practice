'''

    Important learning topic: to find items in, a set is much faster as it uses a hash table to store
    elements.
    'membership testing' is MUCH FASTER. When testing 'A in B', B should be a set or dictionary instead of a list or tuple.

    O(1) vs O(n) as it uses HASH TABLE

    Items are stored based on their HASH - meaning that to look for an item, all a set/dictionary must do is simply 
    hash the element you are searching for and then see if it exists. 
    O(1)!!!
    The same with removing elements.

    HOWEVER. Generally sets are SLOWER than lists/tuples.

    HASH TABLES CANNOT PRESERVE THE ORDER OF INSERTION!!!

'''