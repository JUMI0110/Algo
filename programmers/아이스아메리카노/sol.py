def solution(money):
    answer = []
    if money % 5500 == 0:
        result1 = money // 5500 
        result2 = 0
        answer.append(result1)
        answer.append(result2)
    else:
        result1 = money // 5500
        result2 = money % 5500
        answer.append(result1)
        answer.append(result2)
    return answer


print(solution(5500))
print(solution(15000))