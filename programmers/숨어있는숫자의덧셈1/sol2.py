def solution(my_string):
    answer = 0
    for char in my_string:
        if ord('1') <= ord(char) <= ord('9'):
            answer += int(char)

    return answer

# 아스키 코드 ord()
    
    

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))