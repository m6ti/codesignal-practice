def solution(s):
    return len(set(s))

print(set(['a','a']))

def solution(s):
    chars = []
    for char in s:
        if char not in chars:
            chars.append(char)
    return len(chars)
#My solution ^^