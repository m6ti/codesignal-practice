import string
def solution(name):
    try:
        int(name[0])
        return False
    except:
        for char in name:
            if char.isnumeric() :
                #print("char is ",char,"and IS an int")
                pass
            elif char in string.ascii_lowercase:
                #print("char is ",char,"and IS lowercase")
                pass
            elif char in string.ascii_uppercase:
                #print("char is ",char,"and IS uppercase")
                pass
            elif char == "_":
                print("char is ",char,"and IS an underscore")  
                pass
            else:
                print("we are not liking the character:",char)
                return False
        return True

'''
    The problem here was that I was checking for if a character was numeric by
    checking if it was 'in int', which is incorrect syntax. This is big nono.
    We can simply use the in-built string method isNumeric() to check if a character is numeric.
'''

def isNumber(string):
    print(string.isnumeric())

while(True):
    string = input("Enter a value: ")
    isNumber(string)
















sentence = "pablo shush"

def solution(name):
    try:
        (int(name[0]))
        return False
    except:
        return True
        

print(solution("Pawel"))


flag = False
while(flag == False):
    try:
        age = int(input("enter your age"))
        flag = True
    except:
        print("You entered the wrong age fool.")
print("You entered age:",age)