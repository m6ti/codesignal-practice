def solution(inputString):
    return "".join([increasebyone(x) for x in inputString])    

def increasebyone(letter):
    num = ord(letter)
    if num == 122:
        num = 97
    else:
        num += 1
    return chr(num)

print(solution("pawel"))

#Ceasar shift