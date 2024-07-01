# 받은 문자열에서 숫자 찾기 숫자라면?표현

def solution(my_string):
    answer = 0
    for char in my_string:
        if char.isdigit():
            answer += int(char)

    return answer


    
    

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))